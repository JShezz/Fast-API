from datetime import datetime

from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database import Base


class BaseMixin(Base):

    __abstract__ = True

    created_at = Column(String, default=datetime.utcnow)
    last_updated_at = Column(String, default=datetime.utcnow, onupdate=datetime.utcnow)

    def add(self, db: Session):
        db.add(self)
        return self.save(db=db)

    def delete(self, db: Session):
        db.delete(self)
        db.commit()

    def update(self, db: Session, payload: BaseModel | dict):
        payload = payload if isinstance(payload, dict) else vars(payload)
        for key, value in payload.items():
            setattr(self, key, value)
        return self.save(db=db)

    def save(self, db: Session):
        try:
            db.commit()
            db.refresh(self)
            return self
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(400, str(e.orig))


class User(BaseMixin):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

