from datetime import datetime
from sqlalchemy import VARCHAR, BigInteger, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text

Base = declarative_base()


class BaseEntity:
    id = Column('id', BigInteger, primary_key=True, autoincrement=True)

    createdAt = Column(
        'created_at', DateTime, nullable=False,
        server_default=text("TIMEZONE('utc', CURRENT_TIMESTAMP)")
    )
    updatedAt = Column(
        'updated_at', DateTime, nullable=False,
        server_default=text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f"{self.__class__.__name__}<id={self.id}>"


class User(Base, BaseEntity):
    __tablename__ = "user"

    firstName = Column('first_name', VARCHAR(255), nullable=False)
    lastName = Column('last_name', VARCHAR(255), nullable=False)
    email = Column('email', VARCHAR(255), nullable=False)
