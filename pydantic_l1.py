from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional

#creating pydantic model
class Patient(BaseModel):

    name: str
    age:  int = Field(gt=0, lt=65)
    email :EmailStr
    weight: float = Field(gt=0)
    married: bool
    allergies :Optional[List[str]] = None  #made this field optional, default value needs ot be set to none.
    contact : Dict[str, str]

#raw input
patient_info = {
    'name' : 'Aquib',
    'age' : 25,
    'email' : 'ansari1@yopmail.com',
    'weight': 83.2,
    'married' : False,
    # 'allergies' : ['flu', 'peanut-allergy'],
    'contact' : {'phone' : '03343212158', 'email': 'abc@hotmail.com'}
}

#creating the pydantic model's object
patient1 = Patient(**patient_info)

#passing that model's object to a function
def insert_patients(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact)
insert_patients(patient1)


