from pydantic import BaseModel


class ContactForm(BaseModel):
    id: int
    name: str
    email: str
    message: str
    
