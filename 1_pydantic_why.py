from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


# Field is use to give the validation to the data which we are getting from the user

class Patient(BaseModel):
    name : Annotated[str , Field(max_length = 50, title = 'name of the patient', description= 'give the name of the patient in less than 50 chars', examples = ['nitish','amit'])] # here we use annotation to give the meta  data to the field
    email: EmailStr
    linked_url : AnyUrl
    age : int = Field(gt =0, lt = 100) 
    weight : float = Field(gt =0)
    married : bool = False # here we are giving default value to married if someone is not using it it shows false
    allergies : Optional[List[str]] = None # here we use optional which means if someone is not using the allergies part it shows none
    contact_details : Dict[str,str]
# we use to attach the meta data by using Annotated and Field
#Meta data means adding the description ,title and the example to that particular field 

#function to insert the patient data
# def insert_patient_data(patient: Patient):
#     print(patient.name)
#     print(patient.age)
#     print("inserted")


#function to update the patient data
def updated_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient.linked_url)
    print("updated")


patient_info = {'name':'nitish','age' : 30, 'email': 'abc@gmail.com' , 'linked_url' : 'https://linkedin.com/123','weight' : 75, 'married': 1,'allergies' : ['pollen' , 'dust'] , 'contact_details' : { 'number':'6394545'}} #dictionary data

# with the help of this dictionary we instatiate the python object

patient1 = Patient(**patient_info)#object

updated_patient_data(patient1)

