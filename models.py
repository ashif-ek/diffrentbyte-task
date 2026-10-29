from database import Base
from sqlalchemy.orm import Mapped, mapped_column

class Forms(Base):
    __tablename__ = "my_form"
    id: Mapped[int] = mapped_column(primary_key = True)
    nmae: Mapped[str]
    email: Mapped[str]
    message: Mapped[str]

