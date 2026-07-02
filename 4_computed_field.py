from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List, Dict


class Patient(BaseModel):
    name : str
    email: EmailStr
    linked_url : AnyUrl
    height : float
    age : int
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str,str]

    @computed_field
    @property
    def calculate_bmi(self)-> float:
        bmi = round((self.weight / self.height**2),2)
        return bmi
    

        
        



def updated_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI',patient.calculate_bmi)
    print("updated")

patient_info = {'name':'nitish','age' : 70, 'email': 'abc@gmail.com', 'height': 1.72 ,'linked_url' : 'https://linkedin.com/123', 'weight' : 75, 'married': 1,'allergies' : ['pollen' , 'dust'] , 'contact_details' : { 'number':'6394545','emergency_contact': '904425'}} 
#dictionary data

patient1 = Patient(**patient_info) 

updated_patient_data(patient1)
