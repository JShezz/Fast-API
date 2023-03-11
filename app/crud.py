from fastapi import HTTPException
from sqlalchemy.orm import Session

from database import query_single_model


def create(db, payload, model):
    new_model = model(**payload.dict())
    return new_model.add(db)


def read_by_column(db: Session, model_to_query, model_attribute, value):
    model = query_single_model(db, model_to_query, model_attribute, [model_attribute == value])
    if model is None:
        raise HTTPException(
            status_code=404,
            detail=f"No {model_to_query.__name__} found with the {model_attribute.name} {value}.")
    return model


def read_all(db: Session, model_to_query):
    return db.query(model_to_query).all()


def update(db: Session, payload, model_to_query, model_attribute, value):
    model = read_by_column(db, model_to_query, model_attribute, value)
    return model.update(db, payload.dict(exclude_unset=True))


def delete(db: Session, model_to_query, model_attribute, value):
    model = read_by_column(db, model_to_query, model_attribute, value)
    model.delete(db)



