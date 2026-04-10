# 🎵 Music Recommender Simulation

## Project Summary

This project simulates a small content-based music recommender. My version uses song attributes like genre, mood, energy, and acousticness to compare each track against a user taste profile. It gives every song a weighted score, ranks the catalog from highest to lowest, and returns the top recommendations with short explanations for why each song matched.

---

## How The System Works

Real recommendation systems often use both user behavior and content features to predict what someone may like next. My version is a simple content-based recommender, so it only looks at song attributes and user preferences instead of using data from other listeners.

The recommender gives each song points for matching genre and mood, then adds a similarity score based on how close the song's energy is to the user's target. It also adds a small bonus or penalty based on acousticness. After scoring every song, it sorts them from highest to lowest and returns the top results.

Algorithm recipe:
- +2.0 for genre match
- +1.5 for mood match
- up to +2.0 for energy closeness
- up to +1.0 based on acousticness preference

This design is easy to understand, but it may over-prioritize genre and may miss songs that feel right for a user in more subtle ways.

### Planned User Profile

Example profile:

```python
{
    "favorite_genre": "lofi",
    "favorite_mood": "chill",
    "target_energy": 0.35,
    "likes_acoustic": True
}
```

Planned Song features:
- genre
- mood
- energy
- tempo_bpm
- valence
- danceability
- acousticness

Planned UserProfile features:
- favorite_genre
- favorite_mood
- target_energy
- likes_acoustic

Mermaid representation of data flow:
graph TD;
    A[User Preferences] --> B[Load Songs];
    B --> C[Score Each Song];
    C --> D[Rank Songs];
    D --> E[Return Top K Recommendations];


---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this