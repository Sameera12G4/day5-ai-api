from fastapi import FastAPI
from models import Student
from models import TextData
from models import CalculateData
from models import PromptData
from services import analyze_text
from services import calculate
from services import generate_response
app = FastAPI()
students = [
    {
        "id": 1,
        "name": "Sameera",
        "department": "CSE",
        "marks": 85,
        "email": "sameera@gmail.com"
    },
    {
        "id": 2,
        "name": "Swetha",
        "department": "IT",
        "marks": 89,
        "email": "swetha@gmail.com"
    }
]
@app.get("/health")
def health():
    return {"status": "API is running"}
@app.get("/students")
def get_students():
    return students
@app.get("/students/{id}")
def get_student(id: int):
    for student in students:
        if student["id"] == id:
            return student
    return {"message": "Student not found"}
@app.post("/students")
def create_student(student: Student):
    students.append(student.model_dump())
    return {
        "message": "Student added successfully",
        "student": student
    }
@app.post("/analyze-text")
def analyze_text_api(data: TextData):
    return analyze_text(data.text)
@app.post("/calculate")
def calculate_api(data: CalculateData):
    result = calculate(
        data.number1,
        data.number2,
        data.operation
    )
    if result is None:
        return {"message": "Invalid operation"}

    return {"result": result}
@app.post("/generate")
def generate(data: PromptData):

    response = generate_response(data.prompt)

    return {
        "prompt": data.prompt,
        "response": response
    }