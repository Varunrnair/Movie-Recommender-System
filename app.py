import streamlit as st
import pandas as pd
import pickle
import requests

similarity = pickle.load(open('similarity.pkl','rb')) 
movie_dict = pickle.load(open('movie_dict.pkl','rb')) 
movies= pd.DataFrame(movie_dict)

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=dee79f21ce41729524b185a07e0c28d2&language=en-US'.format(movie_id))
    response=response.json()
    return 'https://image.tmdb.org/t/p/w500' + response['poster_path']

def recommend(movie):
    name=[]
    poster=[]
    movie_index=movies[movies['title']==movie].index[0]
    movie_similarity=similarity[movie_index]
    movie_similarity=sorted(list(enumerate(movie_similarity)),reverse=True,key=lambda x:x[1])
    for i in movie_similarity[1:11]:
        movie_id=movies.iloc[i[0]].movie_id
        name.append(movies.iloc[i[0]].title)
        poster.append(fetch_poster(movie_id))
    return name,poster

st.title('Movie Recommender System')

selected_movie = st.selectbox(
    'Select a Movie',
    movies['title'].values)

if st.button('Recommend'):
    name,poster=recommend(selected_movie)
    col1, col2, col3, col4, col5= st.columns(5)
    st.divider() 
    col6, col7, col8, col9, col10= st.columns(5)
    st.divider() 
    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])  
     
    with col4:
        st.text(name[3])
        st.image(poster[3])   
        
    
    with col5:
        st.text(name[4])
        st.image(poster[4])

    with col6:
        st.text(name[5])
        st.image(poster[5])

    with col7:
        st.text(name[6])
        st.image(poster[6])

    with col8:
        st.text(name[7])
        st.image(poster[7])

    with col9:
        st.text(name[8])
        st.image(poster[8])

    with col10:
        st.text(name[9])
        st.image(poster[9])