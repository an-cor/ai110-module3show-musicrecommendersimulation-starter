# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

This recommender has a few clear limitations. The biggest one is that it can over-prioritize genre, which may push songs from the favorite genre to the top even when other songs have a better mood or energy match. 

The system also works on a very small catalog, so some genres and moods are underrepresented. Because of that, the recommender can create a small filter bubble where similar songs keep appearing and variety is limited. It also assumes music taste can be captured with only a few features, which leaves out things like lyrics, artist preference, and listening context.

---

## 7. Evaluation  

I tested the recommender with several profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and an edge-case profile with sad mood but high energy. I looked at whether the top 5 songs felt reasonable based on the profile and whether the same songs kept appearing too often.

The results mostly matched my expectations. High-Energy Pop favored upbeat, energetic songs like "Sunrise City" and "Gym Hero." Chill Lofi shifted toward lower-energy and more acoustic songs, which made sense. The edge-case profile was useful because it showed how the scoring logic can struggle when mood and energy point in different directions.

I also ran a small experiment where I reduced the genre weight and increased the energy weight. That change made the recommendations more varied and more sensitive to energy, but it also made the system feel less anchored to the user’s stated genre preference. This showed me that small weight changes can strongly affect the behavior of the recommender.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
