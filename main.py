from fastapi import FastAPI, Path, Query, HTTPException
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
@app.get('/view/{patient_id}') #route defined  with path param dynamically
def view_patient(patient_id: str = Path(..., description= 'ID of the patient in the db', example= 'P001')):
    data = load_data() #load all the patients
    if patient_id in data:
        return data[patient_id]
    
    raise HTTPException(status_code=404, detail='patient not found')

#sorting patients using query paramters;
#three dots meaning it is required and not means it is optional
@app.get('/sort')
def sort_patients(sortBy:str = Query(..., description='Sort on the basis of height, weight or BMI'), orderBy:str = Query('asc', description='Sort in ascending or descending order')):

    valid_fields = ["height", "weight", "bmi"]
    if sortBy not in valid_fields:
        raise HTTPException(status_code=400, detail=f'invalid field select from {valid_fields}') #bad request
    
    if orderBy not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='invalid order, select  asc or desc ')
    
    data = load_data()
    sort_order = True if orderBy=='desc' else False
    sorted_data = sorted(data.values(), key=lambda x:x.get(sortBy,0), reverse=sort_order)

    return sorted_data
      




