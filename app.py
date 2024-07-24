import streamlit as st
import pickle
import requests

st.header("movies Recommendation ystem Using Machine Learning")
movies=pickle.load(open('artificates/movie_list.pkl','rb'))
similarity=pickle.load(open('artificates/similarity.pkl','rb'))

st.title('Movies Recommender System')
movies_list=movies['title'].values
selected_movie =st.selectbox(
     'Type or select Movie to get recommendation',
    movies_list
)
def fetch_poster(movies_id):
        url="https://api.themoviedb.org/3/movie/{}?api_key=46cac56ef18da50841a58c3e84a8ad41&append_to_response=videos".format(movies_id)
        data =requests.get(url)
        data=data.json()
        poster_path=data['poster_path']
        full_path="http://image.tmdb.org/t/p/w500/"+poster_path
        return full_path

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    recommended_movies_name=[]
    recommended_movies_poster=[]

    for i in distance[1:6]: 
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name,recommended_movies_poster

if st.button('show recommendation'):
    recommended_movies_name,recommended_movies_poster=recommend(selected_movie)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0])
    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1])
    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2])
    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3])
    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4])

 