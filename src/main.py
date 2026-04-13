"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs

def print_recommendations(profile_name: str, user_prefs: dict, songs: list[dict]) -> None:
    print("=" * 72)
    print(profile_name)
    print(f"prefs: {user_prefs}")
    print("=" * 72)

    recommendations = recommend_songs(user_prefs, songs, k=5)

    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{i}. {song['title']} by {song['artist']}")
        print(f"   score: {score:.2f}")
        print(f"   reasons: {explanation}")
        print()

    print()

def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}\n")

    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8,
            "likes_acoustic": False,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35,
            "likes_acoustic": True,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.95,
            "likes_acoustic": False,
        },
        "Edge Case: Sad but High Energy": {
            "genre": "pop",
            "mood": "sad",
            "energy": 0.9,
            "likes_acoustic": False,
        },
    }

    for profile_name, prefs in profiles.items():
        print_recommendations(profile_name, prefs, songs)


if __name__ == "__main__":
    main()
