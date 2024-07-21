import streamlit as st
import pandas as pd
# Task 4
movies_df = pd.read_csv('movies.csv')

st.title('Movie  Recommendation system')

User_Input = st.text_input('Enter a genre (e.g., Comedy, Drama,Fantasy,Children):')

def SuggestMovie(User_Input, movies_df):
    similar_movies = movies_df[movies_df['genres'].str.contains(User_Input, case=False)]
    return similar_movies.head(5)


if User_Input:
    st.header(f'Movies in {User_Input} genre:')
    recommended_movies = SuggestMovie(User_Input, movies_df)
    for index, row in recommended_movies.iterrows():
        st.write(f"**{row['title']}** - *Genres: {row['genres']}*")
else:
    st.info('Enter a genre to get recommendations.')

# Footer
st.markdown('---')

