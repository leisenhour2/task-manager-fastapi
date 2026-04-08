from models import Task, TaskCreate, TaskUpdate
from fastapi import FastAPI
from typing import List
import crud

# Create FastAPI application instance
app = FastAPI()


# =========================
# CREATE (POST)
# =========================
# Endpoint: POST /tasks
# Receives task data from request body (TaskCreate model)
# Calls CRUD function to insert task into database
@app.post("/tasks")
def create_task(task: TaskCreate):
    return crud.create_task(task)


# =========================
# READ (GET)
# =========================
# Endpoint: GET /tasks
# Returns all tasks from database
# response_model ensures output is a list of Task objects
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return crud.get_tasks()


# =========================
# UPDATE (PATCH)
# =========================
# Endpoint: PATCH /tasks/{task_id}
# task_id comes from URL path
# task (TaskUpdate) comes from request body
# Passes both to CRUD to update database
@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    return crud.update_task(task, task_id)  


# =========================
# DELETE (DELETE)
# =========================
# Endpoint: DELETE /tasks/{task_id}
# task_id comes from URL path
# Calls CRUD function to delete task from database
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    return crud.delete_task(task_id)