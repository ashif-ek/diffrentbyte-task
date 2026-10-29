from pydantic import BaseModel

class FormCreate(BaseModel):
    name: str
    email: str
    message: str