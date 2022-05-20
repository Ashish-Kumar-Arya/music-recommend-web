import webbrowser
import streamlit as st
import pickle
st.title('Song Recommender System')
def recommend(song):
    song_index = songs[songs['song']==song].index[0]
    distances = similarity[song_index]
    songs_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
    recommended_songs = []
    for i in songs_list:
        recommended_songs.append(songs.iloc[i[0]].song)
    return recommended_songs

def index(song):
    return songs[songs['song']==song].index[0]

songs = pickle.load(open('songs.pkl','rb'))
songs_list = songs['song'].values

similarity = pickle.load(open('similarity.pkl','rb'))

selected_song = st.selectbox(
'Select a song',
songs_list)

if st.button('Recommend'):
    recommendations = recommend(selected_song)
    for i in recommendations:
        st.write(i)
        ws = "%20".join(i.split())
        link = (f"https://www.google.com/search?q={ws}")
        st.markdown(link, unsafe_allow_html=False)



