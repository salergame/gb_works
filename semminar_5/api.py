from fastapi import APIRouter, HTTPException
from typing import List
from semminar_5.models import Task

router = APIRouter()

tasks = []

@router.get("/tasks", response_model=List[Task])
async def read_tasks():
    return tasks

@router.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    task = next((task for task in tasks if task.get("id") == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/tasks", response_model=Task)
async def create_task(task: Task):
    task_dict = task.dict()
    task_dict["id"] = len(tasks) + 1
    tasks.append(task_dict)
    return task_dict

@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    index = task_id - 1
    if index < 0 or index >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[index] = task.dict()
    tasks[index]["id"] = task_id
    return tasks[index]

@router.delete("/tasks/{task_id}", response_model=Task)
async def delete_task(task_id: int):
    index = task_id - 1
    if index < 0 or index >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    deleted_task = tasks.pop(index)
    return deleted_task
