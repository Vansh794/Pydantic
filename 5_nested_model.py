from pydantic import BaseModel

class Address(BaseModel):
    state : str
    city : str
    pincode : str


class Patient(BaseModel):
    name : str
    age : int 
    gender : str
    address : Address

address_dict = { 'city' : 'gurgaon' , 'state' : 'haryana' , 'pincode' : '122001'}

address1 = Address(**address_dict)


patient_dict = {'name' : 'nitish' , 'gender' : 'male' , 'age' : 29 , 'address' : address1}


patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)