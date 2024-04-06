from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    # email = Column(String, unique=True, index=True)
    is_verified = Column(Boolean, default=False)
    phone_number = Column(String)
    hashed_password = Column(String)
    area_id = Column(Integer, ForeignKey("area.id"))

    area = relationship("Area", back_populates="users")

    permission = Column(String, default="base")


class Area(Base):
    __tablename__ = "area"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True, unique=True)
    position = Column(String, unique=True)

    users = relationship("User", back_populates="area")


class Temperature(Base):
    __tablename__ = "temperature"

    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(String, unique=True)
    data = Column(Integer)
    is_warning = Column(Boolean, default=False)


class Pressure(Base):
    __tablename__ = "pressure"

    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(String, unique=True)
    data = Column(Integer)
    is_warning = Column(Boolean, default=False)


class Smoke(Base):
    __tablename__ = "smoke"

    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(String, unique=True)
    is_warning = Column(Boolean, default=False)


class OperateLog(Base):
    __tablename__ = "operate_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    data = Column(String)
