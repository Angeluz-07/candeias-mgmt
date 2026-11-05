from src.infra.postgres.repo import PostgresRepository
from src.infra.postgres.models import MemberBase
from src.domain.models import Member


class MemberService:

    def __init__(self, repo: PostgresRepository):
        self.repo = repo

    # def add_member(self, name: str, email: str, phone: str) -> bool:
    #     item = Member(name, email, phone)
    #     return self.repo.add(item)

    def get_all(self):
        result = []
        db_result = self.repo.get_all()
        for x in db_result:
            m = self._map_db_to_domain(x)
            result.append(m)
        return result

    def _map_domain_to_db(self, item: Member):
        return MemberBase(
            name=item.name,
            email=item.email,
            phone=item.phone,
            id=item.id,
            created_at=item.created_at,
        )

    def _map_db_to_domain(self, item: MemberBase):
        return Member(
            name=item.name,
            email=item.email,
            phone=item.phone,
            id=item.id,
            created_at=item.created_at,
        )

    def add_member(self, name: str, email: str, phone: str):
        m = Member(name, email, phone)
        item = self._map_domain_to_db(m)
        self.repo.add(item)
        return m
