from pydantic import BaseModel, EmailStr, AnyUrl, field_validator
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

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdfc.com', 'icici.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('not a valid email domain')
        return value
    

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age',mode = 'before')
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('age must be between 0 to 100')



def updated_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.linked_url)
    print("updated")

patient_info = {'name':'nitish','age' : 30, 'email': 'abc@hdfc.com', 'linked_url' : 'https://linkedin.com/123', 'weight' : 75, 'married': 1,'allergies' : ['pollen' , 'dust'] , 'contact_details' : { 'number':'6394545'}} 
#dictionary data

patient1 = Patient(**patient_info) #validation -> type coersion

updated_patient_data(patient1)
