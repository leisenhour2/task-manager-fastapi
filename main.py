from models import Task, TaskCreate
from fastapi import FastAPI
from typing import List
import crud

app = FastAPI()

@app.post("/tasks")
def create_task(task: TaskCreate):
    return crud.create_task(task)

@app.get("/tasks", response_model = List[Task])
def get_tasks():
    return crud.get_tasks()


