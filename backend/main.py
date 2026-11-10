from fastapi import FastAPI

klu = FastAPI(title="AI Tutor",
              description="AI Tutor PBL Project",
              version="1.0.0")

@klu.get("/")
def home():
    return {"message":"Welcome to AI Tutor Project"}

@klu.get("/demo")
def demo():
    return {"message":"KL university"}

@klu.get("/askquestion")
def ask():
    return {"message":"What is LLM","Answer":"Large Language Model"}

@klu.get("/student")
def student():
    return {"id":1,"name":"Sai","gender":"male","course":"DSA"}

@klu.get("/students")
def getstudents():
    return [
        {"id":1,"name":"Sai","gender":"male","course":"DSA"},
        {"id":2,"name":"Dattu","gender":"male","course":"DSA"},
        {"id":3,"name":"Karthik","gender":"male","course":"DSA"},
    ]
