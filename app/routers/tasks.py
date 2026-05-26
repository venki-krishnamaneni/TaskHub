from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.logger import logger
from app.database import SessionLocal
from app import models, schemas

router = APIRouter()

# DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Task
@router.post("/tasks")
def create_task(task: schemas.Task, db: Session = Depends(get_db)):

    new_task = models.TaskModel(
        title=task.title,
        description=task.description,
        status=task.status
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    logger.info(f"Task created with ID: {new_task.id}")
    return {
        "message": "Task created successfully",
        "task": {
            "id": new_task.id,
            "title": new_task.title,
            "description": new_task.description,
            "status": new_task.status
        }
    }

# Get Tasks
@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):

    tasks = db.query(models.TaskModel).all()

    task_list = []

    for task in tasks:
        task_list.append({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status
        })
    logger.info("Fetched all tasks")
    return task_list

# Update Task
@router.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: schemas.Task,
                db: Session = Depends(get_db)):

    task = db.query(models.TaskModel).filter(
        models.TaskModel.id == task_id
    ).first()

    if not task:
        logger.error(f"Task not found with ID: {task_id}")
        raise HTTPException(
            status_code=404,
            detail="Task not found"
    )

    task.title = updated_task.title
    task.description = updated_task.description
    task.status = updated_task.status

    db.commit()
    db.refresh(task)
    logger.info(f"Task updated with ID: {task.id}")
    return {
        "message": "Task updated successfully"
    }

# Delete Task
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(models.TaskModel).filter(
        models.TaskModel.id == task_id
    ).first()

    if not task:
        logger.error(f"Task not found with ID: {task_id}")
        raise HTTPException(
            status_code=404,
            detail="Task not found"
    )

    db.delete(task)
    db.commit()
    logger.info(f"Task deleted with ID: {task.id}")
    return {
        "message": "Task deleted successfully"
    }