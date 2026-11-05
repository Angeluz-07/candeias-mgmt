from src.config import POSTGRES_URI


def get_db_session():
    from src.infra.postgres.repo import get_postgres_session
    from src.config import POSTGRES_URI

    return get_postgres_session(POSTGRES_URI)


def get_member_service():
    from src.services.member import MemberService
    from src.infra.postgres.repo import PostgresRepository
    from src.infra.postgres.models import MemberBase

    session = next(get_db_session())

    repo = PostgresRepository(session, MemberBase)
    service = MemberService(repo)
    return service


class APIContext:
    def __init__(self):
        self.member_service = get_member_service()
