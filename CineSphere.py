import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image
import os

movie_icon = Image.open('icon.png')

st.set_page_config(
    page_title="CineSphere",
    page_icon=movie_icon,
)

page_bg = """
<style>
div.stButton > button:first-child {
    background-color: #b3306b;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #070217;
    color:#ffffff;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
[data-testid="stAppViewContainer"] {

background-image: url("https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=1925&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;

}

[data-testid="stVerticalBlockBorderWrapper"] {
border-style: solid;
    border-color: aliceblue;
  margin: 1em;
  padding: 2em;
  background: #070217;
  color: white;
  border-radius: 30px;
  width: 100%;
  max-width: 1200px;
  opacity: 0.9;
}
    
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

def fetch_movie_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c32865d4c49c2b065ce3a552a4212b64&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),
                        reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_movie_poster(movie_id))
    return recommended_movies, recommended_movies_poster

# Function to download file from Google Drive
def download_file(url, dest):
    with requests.get(url, streamlit=False) as response:
        response.raise_for_status()
        with open(dest, 'wb') as f:
            f.write(response.content)

# URL to the file in Google Drive
FILE_ID = 'https://drive.google.com/file/d/141K395I6qcLj_ixUbvLNTS-XipM6Nk_k/view?usp=drive_link' 
FILE_URL = f'https://drive.google.com/uc?export=download&id={FILE_ID}'
FILE_NAME = 'similarity.pkl'

# Check if the file exists, if not, download it
if not os.path.exists(FILE_NAME):
    st.write(f"Downloading {FILE_NAME} from Google Drive...")
    download_file(FILE_URL, FILE_NAME)
    st.write(f"{FILE_NAME} downloaded.")

movie_dictionary = pickle.load(open('movies_dictionary.pkl', 'rb'))
movies = pd.DataFrame(movie_dictionary)
similarity = pickle.load(open(FILE_NAME, 'rb'))

st.header('CineSphere: Movie Recommender System')

selected_movie = st.selectbox(
    'Which movie would you like to see?',
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
