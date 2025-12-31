import pickle
import pandas as pd
from config.MovList import Movies

with open('model/similarity.pkl','rb') as f:
    model=pickle.load(f)

def Predict(title:str):
    match = Movies[Movies["title"]== title]
    movie_i = match.index[0]

    distances = list(enumerate(model[:, movie_i]))
    m_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:10]
    recommended= [
        Movies.iloc[i[0]]["title"] for i in m_list
    ]
    return {"recommended_movies":recommended}