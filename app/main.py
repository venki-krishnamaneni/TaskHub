from fastapi import FastAPI
from app.logger import logger
from app.database import engine
from app import models
from app.routers import tasks
from app.database import SessionLocal
from sqlalchemy import text

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tasks.router)
#home API
@app.get("/")
def home():
    return {"message": "Task Management API is running"}

@app.get("/health")
def health_check():

    logger.info("Health check endpoint called")

    return {
        "status": "healthy"
    }


@app.get("/ready")
def readiness_check():

    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))

        logger.info("Readiness check passed")

        return {
            "status": "ready"
        }

    except Exception as e:

        logger.error(f"Readiness check failed: {str(e)}")

        return {
            "status": "not ready"
        }

    finally:
        db.close()