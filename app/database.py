from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def query_single_model(db: Session, model, model_attribute=None, identifier=None, filters: list = None):
    """
    :param db: SQLALchemy Session
    :param model: Example - SQLAlchemy Model Class
    :param model_attribute: Example.id
    :param identifier: 1 - Any type of unique model key
    :param filters: [Example.title == "example_title", Example.is_active == True] - Any list of model filters
    :return:
    """
    query = db.query(model) if not isinstance(model, list) else db.query(*model)
    _filters = []
    if model_attribute:
        _filters.append(model_attribute == identifier)
    else:
        _filters = filters

    return query.first()
