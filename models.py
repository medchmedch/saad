from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    age = Column(Integer, nullable=False)


    def __repr__(self):
        return f"<User name={self.name} age={self.age}>"
