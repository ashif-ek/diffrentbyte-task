from fastapi import FastApi, Form 
from models import Forms
from database import Depends, db_get, engine

Base.metadata.create_all(bind=engine)

app = FastApi()


@app.post("/forms")
def form_create(data: Forms, db: Session = Depends(de_get) ):
    form = Forms(**data.model_dump)
    db.add(form)
    db.commit()
    db.refresh(form)
    return form
