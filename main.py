from fastapi import FastAPI
import pickle
from schemas import ModelInput

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


app = FastAPI(title="Diabetes Prediction API")

diabetes_model = pickle.load(open('model/diabetes_model.sav', 'rb'))

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(data: ModelInput):

    input_list = [
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]

    prediction = diabetes_model.predict([input_list])

    result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"

    return {"prediction": result}
