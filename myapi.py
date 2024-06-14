from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel 
# To run using unicorn :
# uvicorn myapi:app --reload

app = FastAPI()

students = {
    1 : {
        "name" : "John",
        "age" : 17,
        "year" : "year 12"
    }
}

class Student(BaseModel):
    name : str
    age : int
    year : str

# for the PUT method, we will use this class to update the data
# we will use Optional to make the fields optional. So we do not have to update all fields at once.
class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None

# home page
@app.get("/")
def index():
    return {"name" : "First data"}

# fast api uses JSON response by default, we will use dict soon
# Path parameters -> get std data for 1 from dict on url, ex : google.com/get-student or 1
# description is for the docs. It helps understand the parameter. 
# we also try gt, lt, ge, le, ne, gtlt, gele, gtge, ltlt, ltgt, lege, lene, nelt, nelt, nege??
# we get the errors according to the constraints we set.

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path( description="The ID of the student you want to view", gt=0 , lt=3)):
    return students[student_id]

# Query parameters = pass value into a url using ?key=value , ex : google.com/get-student?student_id=1
# it is on the same endpoint. 

# try this code below ------------------------------

# @app.get("/get-by-name")
# def get_student(* , name : Optional[str] = None, test : int): # = None is default value, also Optional is used to make it optional
#     for student_id in students:
#         if students[student_id]["name"] == name:
#             return students[student_id]
#     return {"Data" : None}    

# SyntaxError: non-default argument follows default argument. remember to put the default argument at the end.

# combine path and query parameters as shown below
  
@app.get("/get-by-name/{student_id}")
def get_student(* ,student_id: int, name : Optional[str] = None, test : int): 
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : None}    

# POST method - to add data to the dict
# remember that it is stored in memory, so it will be lost when the server is restarted.
# we can use a database to store the data permanently. 
@app.post("/create-student/{student_id}")
def create_student(student_id:int, student : Student):
    if student_id in students:
        return {"Error" : "Student exists"}
    students[student_id] = student
    return students[student_id]

# PUT method - to update data in the dict
@app.put("/update-student/{student_id}")
def update_student(student_id:int, student : UpdateStudent):
    if student_id not in students:
        return {"Error" : "Student does not exist"}

    if student.name != None : 
        students[student_id].name = student.name
    
    if student.age != None :
        students[student_id].age = student.age
    
    if student.year != None :
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error" : "Student does not exist"}
    del students[student_id]
    return {"Message" : "Student deleted successfully"}

