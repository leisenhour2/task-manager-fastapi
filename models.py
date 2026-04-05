from pydantic import BaseModel


class TaskBase(BaseModel):
    task_name: str
    task_desc: str | None = None
    assigned_to: str


class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    task_id: int
    completed: bool
