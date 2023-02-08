from sqlalchemy import Column, Integer, Boolean, String

from app.core.database import Base


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primari_key=True)
    first_name = Column(String(128))
    last_name = Column(String(128))
    username = Column(String(256))
    is_admin = Column(Boolean, nullable=False, default=False)
