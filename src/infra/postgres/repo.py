from typing import Any, Type
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Declarative base central para tus modelos
Base = declarative_base()


def get_postgres_session(database_url: str):
    """Factory function que crea el engine y retorna una sesión limpia."""
    engine = create_engine(database_url, echo=False, pool_pre_ping=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Opcional: crea las tablas si no existen
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


class PostgresRepository:
    def __init__(self, session: Session, model: Type[Any]):
        self.session = session
        self.model = model

    def get_all(self):
        result = self.session.query(self.model).all()
        return result

    def add(self, entity: Type[Any]):
        self.session.add(entity)
        self.session.commit()

    # def get_by_id(self, item_id: int):
    #     return self.session.query(self.model).filter(self.model.id == item_id).first()
