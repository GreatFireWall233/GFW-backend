from sqlalchemy.orm import Session

from utils.encrypt import MD5
from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_phone(db: Session, phone: str):
    return db.query(models.User).filter(models.User.phone_number == phone).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = MD5(user.password)
    db_user = models.User(username=user.username, phone_number=user.phone_number, hashed_password=hashed_password)
    db_user.area_id = user.area_id
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_area(db: Session, area_id: int):
    return db.query(models.Area).filter(models.Area.id == area_id).first()


def get_area_by_name(db: Session, name: str):
    return db.query(models.Area).filter(models.Area.name == name).first()


def get_areas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Area).offset(skip).limit(limit).all()


def create_area(db: Session, area: schemas.Area):
    db_area = models.Area(**area.model_dump())
    db.add(db_area)
    db.commit()
    db.refresh(db_area)

    return db_area
