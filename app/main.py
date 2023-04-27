import joblib
import numpy as np
import sys
sys.path.append("/app/")
from src.models.predict import Model  as PredictRequest
from fastapi import FastAPI
from typing import List
 

#import ml model
model = joblib.load("models/model_v0.pkl")

def predict(input_data):
    # Do your prediction here using the loaded model and input data
    prediction = model.predict(input_data)
    return prediction



app = FastAPI()



@app.post("/predict")
def make_prediction(request: PredictRequest):
    input_data = np.array(list(request.dict().values())).reshape((1,-1))
    prediction = predict(input_data) # Note that we pass a list of lists to the predict function
    return {"prediction": int(prediction[0])}
    #return {"input_data":str(list(input_data))}