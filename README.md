# CineSphere <img src="https://github.com/dhruvi2209/CineSphere/assets/128127602/9eb11430-ae34-44c5-9085-91c9c132397e" alt="icon" width="30" height="30">


Welcome to **Movie Recommender**, a Python project implementing a content-based movie recommendation system. This system leverages text vectorization (Bag of Words) and word stemming using NLTK to suggest movies based on user preferences and movie features such as title, genre, plot summary, and cast.


## Overview

Content-based recommendation systems analyze the attributes of items (in this case, movies) and recommend items with similar attributes to those the user has liked in the past. In this project, we utilize text vectorization (Bag of Words) and word stemming to preprocess textual movie features and recommend similar movies to the user.

![Screenshot 2024-04-05 204833](https://github.com/dhruvi2209/CineSphere/assets/128127602/d41c3007-8a87-42bb-87e0-a31d5f9a1888) <br> <br>

![Screenshot 2024-04-05 204858](https://github.com/dhruvi2209/CineSphere/assets/128127602/301704dd-901a-4a39-a38c-d8a68e42b193) <br> <br>

![Screenshot 2024-04-05 204913](https://github.com/dhruvi2209/CineSphere/assets/128127602/91bf5de8-c769-43df-9f44-e15a448dd964)


## How It Works

The movie recommendation system employs the following steps:

1. **Data Collection:** Gather movie data from various sources, including online databases or APIs. This data includes information about movie titles, genres, plot summaries, and cast.

2. **Data Preprocessing:** Clean and preprocess the movie data. This involves tasks such as removing punctuation, stop words, and performing word stemming using NLTK to normalize the text data.

3. **Text Vectorization (Bag of Words):** Convert the processed text data into numerical vectors using the Bag of Words technique. This approach represents each movie as a vector where each dimension corresponds to a unique word in the corpus, and the value represents the frequency of that word in the movie's text.

4. **Similarity Calculation:** Compute the similarity between movies based on their Bag of Words vector representations. Common similarity measures include cosine similarity and Euclidean distance.

5. **Recommendation Generation:** Given a user's preferences or a selected movie, generate recommendations by finding movies with the highest similarity scores to the user's preferences or the selected movie.

## Usage

To use the Movie Recommender system:

1. **Install Dependencies:** Ensure that you have all the required dependencies installed. You can install them by running:

2. **Run the System:** Execute the main script `CineSphere.py` to run the movie recommendation system:

3. **Input Preferences:** Follow the prompts to input your movie preferences, such as your favourite movie title.

4. **Get Recommendations:** Based on your preferences, the system will generate a list of recommended movies for you to explore.

## Features

- **Customizable Preferences:** Users can input their movie preferences, such as their favourite movie title to receive recommendations.
- **Comprehensive Information:** The recommendation system considers various aspects of movies, including title, genre, plot summary, and cast, to provide diverse and relevant recommendations.
- **Efficient Vectorization:** Utilizes efficient Bag of Words text vectorization technique to represent movie features as numerical vectors, enabling fast similarity calculations and recommendation generation.
- **Word Stemming:** Utilizes NLTK for word stemming to normalize textual data and improve recommendation accuracy.


Enjoy discovering new movies with **Movie Recommender**!

*Developed by Dhruvi Vaghela*
