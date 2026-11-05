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
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


from src.infra.postgres.models import MemberBase, MembershipBase
from src.domain.models import Member, Membership
from sqlalchemy.orm import joinedload


class PostgresMemberRepository:
    def __init__(self, session: Session):
        self.session = session

    def _map_db_to_domain(self, item: MemberBase) -> Member:
        domain_membership = None
        if item.membership:
            domain_membership = Membership(
                id=item.membership.id,
                member_id=item.membership.member_id,
                gym_id=item.membership.gym_id,
                start_date=item.membership.start_date,
                due_date=item.membership.due_date,
                expires_at=item.membership.expires_at,
                cost=item.membership.cost,
            )

        # 3. Mapeamos el Miembro de DB a Dominio inyectándole la membresía
        result = Member(
            id=item.id,
            name=item.name,
            email=item.email,
            phone=item.phone,
            created_at=item.created_at,
            membership=domain_membership,
        )
        return result

    def get_all(self):
        db_members = (
            self.session.query(MemberBase)
            .outerjoin(MemberBase.membership)  # Relación 1 a 1
            .options(joinedload(MemberBase.membership))
            .all()
        )

        domain_members = []
        for db_m in db_members:
            # 2. Mapeamos la membresía de DB a Dominio (si existe)
            domain_member = self._map_db_to_domain(db_m)
            domain_members.append(domain_member)

        return domain_members

    def add(self, entity: Type[Any]):
        self.session.add(entity)
        self.session.commit()

    # def get_by_id(self, item_id: int):
    #     return self.session.query(self.model).filter(self.model.id == item_id).first()
