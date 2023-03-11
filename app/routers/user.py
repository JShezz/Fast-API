from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from dependencies import get_db

router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.UserResponse)
def create_user(payload: schemas.UserBase, db: Session = Depends(get_db)):
    return crud.create(db, payload, models.User)


@router.get("s", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return crud.read_all(db, models.User)


@router.get("/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.read_by_column(db, models.User, models.User.id, user_id)


@router.patch("/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, payload: schemas.UserBase, db: Session = Depends(get_db)):
    return crud.update(db, payload, models.User, models.User.id, user_id)


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete(db, models.User, models.User.id, user_id)





