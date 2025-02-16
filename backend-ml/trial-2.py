from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import extract
from trial1 import SessionLocal, PipelineData  
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/pipeline-data/7-days")
def get_pipeline_data(db: Session = Depends(get_db)):
    try:
        current_time = datetime.now()
        current_hour = current_time.hour
        current_minute = current_time.minute
        rounded_minute = round(current_minute / 10) * 10
        if rounded_minute == 60:  
            rounded_minute = 0
            current_hour = (current_hour + 1) % 24  

        
        results = (
            db.query(PipelineData)
            .filter(extract("hour", PipelineData.timestamp) == current_hour)
            .filter(extract("minute", PipelineData.timestamp) == rounded_minute)
            .filter(PipelineData.pipe_number == 1) 
            .all()
        )

        if not results:
            raise HTTPException(status_code=404, detail="No data found for 11 AM with pipe_number = 1")

        return {"data": results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
