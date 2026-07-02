from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import List, Dict


class Patient(BaseModel):
    name : str
    email: EmailStr
    linked_url : AnyUrl
    age : int
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str,str]

    @model_validator(mode = 'after') #decorator
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency_contact' not in model.contact_details:
            raise ValueError('Patient age more than 60 must have emergency contact')
        return model

        
        



def updated_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.linked_url)
    print("updated")

patient_info = {'name':'nitish','age' : 70, 'email': 'abc@gmail.com', 'linked_url' : 'https://linkedin.com/123', 'weight' : 75, 'married': 1,'allergies' : ['pollen' , 'dust'] , 'contact_details' : { 'number':'6394545','emergency_contact': '904425'}} 
#dictionary data

patient1 = Patient(**patient_info) 

updated_patient_data(patient1)
