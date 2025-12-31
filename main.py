import streamlit as st
import requests
from config.MovList import title_list

FASTAPI_URL = "https://movie-recommender-api-pud9.onrender.com"

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Movie Recommender 🎬",
    page_icon="🎥",
    layout="centered"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main {
    background-color: #0f172a;
    color: white;
}
h1, h2, h3 {
    color: #facc15;
    text-align: center;
}
.stButton>button {
    width: 100%;
    background-color: #facc15;
    color: black;
    font-weight: bold;
    border-radius: 12px;
    padding: 0.6em;
}
.reco-card {
    background: #1e293b;
    padding: 15px;
    margin: 10px 0;
    border-radius: 12px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<h3>Pick a movie and get instant recommendations 🍿</h3>", unsafe_allow_html=True)
st.write("")

# ---------- DROPDOWN ----------
selected_movie = st.selectbox(
    "🎥 Select a movie",
    title_list,
    index=None,
    placeholder="Start typing a movie name..."
)

# ---------- BUTTON ----------
if st.button("🚀 Recommend Movies"):

    if not selected_movie:
        st.warning("⚠️ Please select a movie first")
    else:
        with st.spinner("Finding the best movies for you... 🎞️"):
            response = requests.post(
                f"{FASTAPI_URL}/submit/{selected_movie}"
            ).json()

        if "recommended_movies" in response:
            st.markdown("<h2> ✨ Recommended For You</h2>", unsafe_allow_html=True)

            for movie in response["recommended_movies"]:
                st.markdown(
                    f"<div class='reco-card'>🍿🎥 {movie}</div>",
                    unsafe_allow_html=True
                )
        else:
            st.error(response.get("error", "Something went wrong 😢"))

# ---------- FOOTER ----------
st.write("©️ @Arijit_Chanda")
st.caption("Built with ❤️ using Streamlit & FastAPI")
