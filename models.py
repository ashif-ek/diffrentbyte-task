from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Forms(Base):
    __tablename__ = "forms"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    message: Mapped[str]