from sqlalchemy import Column, Integer, Boolean, String, BigInteger

from app.core.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    username = Column(String(256))
    is_admin = Column(Boolean, nullable=False, default=False)
