from fastapi import FastAPI
import json

app = FastAPI() #object created for fastapi class

@app.get("/") #path endpoint defined route.

#now we createa  functions for this endpoint
def hello():
    return {'message: Patient Management System API'}



@app.get("/about")

def about():
    return{'message': 'A fully functional api to manage your paitent record'}


#loading patients.json file to load data

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    
    return data

# print(load_data())

#view all patients
@app.get("/view")
def view():
    data = load_data()
    return data

#view a particular patient based on id


