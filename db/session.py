from contextlib import contextmanager

from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine("sqlite:///db_with_pornuha.db")

SessionLocal = Session(bind=engine, autocommit=False, autoflush=False)


@contextmanager
def session_scope():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
