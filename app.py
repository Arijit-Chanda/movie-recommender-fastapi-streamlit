from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field
from fastapi.responses import JSONResponse
import json
from config.MovList import Movies,title_list
from model.predict import Predict


MODEL_VERSION='1.0.0'
app=FastAPI()

@app.get('/') #home 
def home():
    return {
        "Message": "🎬 Movie Recommendation System"
    }


@app.get('/health') #health check 
def health():
    return {
        "Status" : "OK",
        "Model Version": MODEL_VERSION,
        "Model Loaded" : "True"
    }


@app.post('/submit/{title}') #Prediction
def predict(title : str):
    match = Movies[Movies["title"]== title]

    if match.empty:
        raise HTTPException(status_code=400,detail="The server cannot process the request due to incorrect syntax or invalid data")

    try :
        recommended_movies = Predict(title)

        return JSONResponse(status_code=200, content=recommended_movies)
    
    except Exception as e:

        return JSONResponse(status_code=500, content=str(e))