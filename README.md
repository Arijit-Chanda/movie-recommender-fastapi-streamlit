# 🎬 Movie Recommendation System

An end-to-end **Movie Recommendation System** built using **FastAPI** for the backend and **Streamlit** for the frontend.  
The system recommends similar movies based on a precomputed similarity matrix.

---

## 🚀 Features
- Searchable movie selection dropdown
- Fast similarity-based recommendations
- REST API using FastAPI
- Interactive Streamlit UI
- Large model file handling using **Git LFS**
- Clean and modular project structure

---

## 🛠️ Tech Stack
- **Backend:** FastAPI, Pydantic
- **Frontend:** Streamlit
- **Data Processing:** Pandas, NumPy
- **Model Storage:** Pickle (`.pkl`) with Git LFS
- **Version Control:** Git & GitHub

---

## 📁 Project Structure
Movie Recommender System/
│
├── app.py # Streamlit app
├── main.py # FastAPI app
├── requirements.txt
├── README.md
├── .gitignore
│
├── config/
│ └── MovList.py
│
└── model/
├── movies.pkl
└── similarity.pkl # Tracked using Git LFS



## ⚙️ How It Works
1. User selects a movie from the Streamlit dropdown.
2. The selected movie title is sent to the FastAPI backend.
3. A similarity matrix is used to find the closest movies.
4. Top recommendations are returned and displayed instantly.

---

## ▶️ Run Locally

### 1️⃣ Clone the repository
```bash
git lfs install
git clone https://github.com/Arijit-Chanda/movie-recommender-fastapi-streamlit.git
cd movie-recommender-fastapi-streamlit


