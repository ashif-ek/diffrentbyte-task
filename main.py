from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, db_get
from models import Forms
from schemas import FormCreate

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/forms")
def create_form(data: FormCreate, db: Session = Depends(db_get)):
    form = Forms(**data.model_dump())
    db.add(form)
    db.commit()
    db.refresh(form)
    return form