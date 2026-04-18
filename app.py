import streamlit as st
import pandas as pd

st.write("🚀 App started")

# Load dataset FIRST (no dependency)
try:
    df = pd.read_csv("movies.csv")
    st.write("✅ Dataset loaded")
except Exception as e:
    st.error(f"CSV Error: {e}")

# UI (force display)
st.title("🎬 Movie Recommendation System")

# Show movies list (to confirm data)
if 'df' in locals():
    st.write("Movies Available:")
    st.write(df)

# Dropdown
if 'df' in locals():
    selected_movie = st.selectbox("Select a movie:", df['title'])

    # Import model ONLY after confirming CSV works
    try:
        from movie_model import recommend
        st.write("✅ Model loaded")
        
        if st.button("Recommend"):
            results = recommend(selected_movie)
            st.subheader("Recommended Movies:")
            for movie in results:
                st.write("👉 " + movie)

    except Exception as e:
        st.error(f"Model Error: {e}")