# Mini AI Backend
A basic FastAPI application for practicing REST APIs.
## APIs
GET /health
GET /students
GET /students/{id}
POST /students
POST /analyze-text
POST /calculate
POST /generate
## Run
uvicorn main:app --reload
## Swagger
http://127.0.0.1:8000/docs