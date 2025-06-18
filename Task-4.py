import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import random

# Sample movie dataset
movies = pd.read_csv(r"D:\Internship files\codsoft\tasks\Task-4 dataset.csv")

# Initialize TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')

tfidf_matrix = tfidf.fit_transform(movies['Description'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get movie recommendations based on content
def get_content_based_recommendations(title, num_recommendations):
    idx = movies.index[movies['Title'] == title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies['Title'].iloc[movie_indices]

# Randomly select a number of recommendations and a movie title
num_recommendations = random.randint(1, 35)  
random_movie_idx = random.randint(0, len(movies) - 1)  
movie_title = movies['Title'].iloc[random_movie_idx] 

# Get recommendations for the randomly selected movie title
recommendations = get_content_based_recommendations(movie_title, num_recommendations)
print(f"Recommendations for '{movie_title}' (Showing {num_recommendations} recommendations):")
print(recommendations)
