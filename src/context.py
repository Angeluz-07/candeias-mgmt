from src.config import POSTGRES_URI


def get_db_session():
    from src.infra.postgres.repo import get_postgres_session
    from src.config import POSTGRES_URI

    return get_postgres_session(POSTGRES_URI)


def get_member_service():
    from src.services.member import MemberService
    from src.infra.postgres.repo import PostgresMemberRepository
    from src.infra.postgres.models import MemberBase

    session = next(get_db_session())

    repo = PostgresMemberRepository(session)
    service = MemberService(repo)
    return service


class APIContext:
    def __init__(self):
        self.member_service = get_member_service()
        self._seed_data()

    def _seed_data(self):
        from src.infra.postgres.models import MemberBase, GymBase, MembershipBase
        from src.domain.models import Member, Gym, Membership
        from dataclasses import asdict

        session = next(get_db_session())

        items = [
            MemberBase(
                name="alfa",
                email="sample1@gmail.com",
                phone="123",
                id="6b442257-f48c-47ec-af90-6f3b7b6a9a69",
                created_at="2026-11-05",
            ),
            MemberBase(
                name="beta",
                email="sample2@gmail.com",
                phone="321",
                id="8e146fa4-4eb1-45c0-8378-df76b9e65e24",
                created_at="2026-11-05",
            ),
            MemberBase(
                name="gama",
                email="sample3@gmail.com",
                phone="456",
                id="2042f5af-7368-409e-a815-142a18712694",
                created_at="2026-11-05",
            ),
            GymBase(
                name="Sede urdesa",
                id="1cff6dcf-944f-4e97-b401-53494c85ee4e",
            ),
            MembershipBase(
                start_date="2026-11-01",
                expires_at="2026-11-30",
                due_date="2026-12-03",
                cost=60,
                gym_id="1cff6dcf-944f-4e97-b401-53494c85ee4e",
                member_id="6b442257-f48c-47ec-af90-6f3b7b6a9a69",
                id="e6708f8b-f18f-46ba-8d39-b97bae95015a",
            ),
        ]
        try:
            # merge() inserta si no existe, o actualiza si ya existe la PK
            for item in items:
                session.merge(item)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error seeding data: {e}")
