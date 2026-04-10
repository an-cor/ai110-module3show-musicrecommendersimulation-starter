from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top-k songs sorted by descending recommendation score."""
        ranked_songs = sorted(
            self.songs,
            key=lambda song: _score_song_object(user, song)[0],
            reverse=True,
        )
        return ranked_songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a short explanation for why a song was recommended."""
        score, reasons = _score_song_object(user, song)
        return f"score={score:.2f}; " + ", ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file into a list of dictionaries.
    Required by src/main.py
    """
    print(f"Loading songs from {csv_path}...")
    songs: List[Dict] = []

    with open(csv_path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    Returns the top-k recommendations as (song, score, explanation) tuples.
    """
    ranked_results: List[Tuple[Dict, float, str]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        ranked_results.append((song, score, explanation))

    ranked_results.sort(key=lambda item: item[1], reverse=True)
    return ranked_results[:k]

def _score_song_object(user: UserProfile, song: Song) -> Tuple[float, List[str]]:
    """Scores one Song object and returns a score with explanation reasons."""
    score = 0.0
    reasons: List[str] = []

    if song.genre.lower() == user.favorite_genre.lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song.mood.lower() == user.favorite_mood.lower():
        score += 1.5
        reasons.append("mood match (+1.5)")

    energy_diff = abs(song.energy - user.target_energy)
    energy_score = max(0.0, 2.0 - (energy_diff * 2.0))
    score += energy_score
    reasons.append(f"energy closeness (+{energy_score:.2f})")

    if user.likes_acoustic:
        acoustic_score = song.acousticness
        score += acoustic_score
        reasons.append(f"acoustic bonus (+{acoustic_score:.2f})")
    else:
        non_acoustic_score = 1.0 - song.acousticness
        score += non_acoustic_score
        reasons.append(f"less-acoustic bonus (+{non_acoustic_score:.2f})")

    return score, reasons

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores one song dictionary against a user preference dictionary."""
    score = 0.0
    reasons: List[str] = []

    if song["genre"].lower() == user_prefs["genre"].lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"].lower() == user_prefs["mood"].lower():
        score += 1.5
        reasons.append("mood match (+1.5)")

    energy_diff = abs(song["energy"] - user_prefs["energy"])
    energy_score = max(0.0, 2.0 - (energy_diff * 2.0))
    score += energy_score
    reasons.append(f"energy closeness (+{energy_score:.2f})")

    if "likes_acoustic" in user_prefs:
        if user_prefs["likes_acoustic"]:
            acoustic_score = song["acousticness"]
            score += acoustic_score
            reasons.append(f"acoustic bonus (+{acoustic_score:.2f})")
        else:
            non_acoustic_score = 1.0 - song["acousticness"]
            score += non_acoustic_score
            reasons.append(f"less-acoustic bonus (+{non_acoustic_score:.2f})")

    return score, reasons    