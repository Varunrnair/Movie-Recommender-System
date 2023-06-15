import streamlit as st
import pandas as pd
import pickle
import requests

similarity = pickle.load(open('similarity.pkl','rb')) 
movie_dict = pickle.load(open('movie_dict.pkl','rb')) 
movies= pd.DataFrame(movie_dict)

def recommend(movie):
    names=[]
    movie_index=movies[movies['title']==movie].index[0]
    movie_similarity=similarity[movie_index]
    movie_similarity=sorted(list(enumerate(movie_similarity)),reverse=True,key=lambda x:x[1])
    for i in movie_similarity[1:10]:
        names.append(movies.iloc[i[0]].title)
    return names

st.title('Movie Recommender System')

selected_movie = st.selectbox(
    'Select a Movie',
    movies['title'].values)

if st.button('Recommend'):
    recommendations=recommend(selected_movie)
    for i in recommendations:
        st.write(i)