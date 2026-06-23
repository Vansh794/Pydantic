from pydantic import BaseModel

class Patient(BaseModel):
    name : str
    age : int
#function to insert the patient data
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("inserted")
#function to update the patient data
def updated_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("updated")


patient_info = {'name':'nitish','age' : 30} #dictionary data

# with the help of this dictionary we instatiate the python object

patient1 = Patient(**patient_info)#object

insert_patient_data(patient1)
updated_patient_data(patient1)

