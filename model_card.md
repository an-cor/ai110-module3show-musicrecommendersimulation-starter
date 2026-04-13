# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeMatch Lite 1.0

---

## 2. Goal / Task

This recommender suggests songs from a small catalog based on a user's preferred genre, mood, energy level, and acoustic preference. It tries to rank songs that best match the user's stated vibe.

---

## 3. Intended Use and Non-Intended Use

### Intended Use

This project is designed for classroom learning and experimentation. It demonstrates how a simple recommendation system can turn user preferences into ranked suggestions.

### Non-Intended Use

This system is not meant for real production users or commercial music platforms. It should not be used to make serious business decisions or to fully represent a person's music taste.

---

## 4. Data Used

The dataset contains 18 songs. It includes features such as:

- genre
- mood
- energy
- tempo_bpm
- valence
- danceability
- acousticness

I expanded the starter dataset by adding more songs and genres such as hip-hop, R&B, folk, EDM, classical, Latin, reggae, and blues.

The dataset is still very small and cannot represent all music tastes or real-world listening behavior.

---

## 5. Algorithm Summary

Each song receives a weighted score based on how well it matches the user profile.

Scoring rules:

- +2.0 points for genre match
- +1.5 points for mood match
- up to +2.0 points based on energy closeness
- up to +1.0 points based on acousticness preference

After every song is scored, the system sorts songs from highest to lowest score and returns the top recommendations.

---

## 6. Observed Behavior / Biases

The recommender works best when the user has clear preferences such as High-Energy Pop or Chill Lofi.

One weakness is that genre can become too important, which may push same-genre songs to the top even when another song better matches mood or energy.

Because the catalog is small, some genres have fewer options than others. This can reduce diversity and create a small filter bubble where similar songs appear often.

The model also ignores many real factors such as lyrics, artist loyalty, listening history, and time of day.

---

## 7. Evaluation Process

I tested the recommender with multiple user profiles:

- High-Energy Pop
- Chill Lofi
- Deep Intense Rock
- Sad but High Energy (edge case)

I checked whether the top recommendations felt reasonable and whether the same songs appeared too often.

I also ran an experiment where I lowered genre weight and increased energy weight. This made recommendations more varied, but less tied to the user's stated genre.

This showed that small weight changes can strongly affect system behavior.

---

## 8. Strengths

- Easy to understand and explain
- Transparent scoring logic
- Produces believable results for clear user profiles
- Fast and simple to run from the command line

---

## 9. Ideas for Improvement

If I continued the project, I would:

- Add a much larger and more diverse dataset
- Include more features such as tempo ranges, favorite artists, or lyrics themes
- Add diversity logic so recommendations are less repetitive
- Learn preferences from listening history instead of only manual inputs

---

## 10. Personal Reflection

My biggest learning moment was seeing how small scoring changes created very different recommendations. Even changing one weight changed the personality of the system.

AI tools helped me move faster when generating ideas, debugging, and improving structure. However, I still needed to double-check the code and logic because generated answers were not always aligned with my intended design.

What surprised me most was how simple math can still feel personalized. Even a weighted scoring system can seem smart when it matches a user's vibe.

If I extended this project, I would explore hybrid recommendation systems that combine user history with song features.