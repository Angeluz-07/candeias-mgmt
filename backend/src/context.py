from src.repositories.user_repository import (
    InMemoryUserRepository,
    FirebaseUserRepository,
)
from src.repositories.student_repository import (
    InMemoryStudentRepository,
    FirebaseStudentRepository,
)
from src.services.auth_service import AuthService
from src.services.student_service import StudentService
from src.domain.models import User, Student
from config import ENVIRONMENT


class AppContext:
    def __init__(self):
        # self.user_repo = InMemoryUserRepository()
        # self.student_repo = InMemoryStudentRepository()

        self.user_repo = FirebaseUserRepository()
        self.student_repo = FirebaseStudentRepository()

        self.auth_service = AuthService(user_repository=self.user_repo)
        self.student_service = StudentService(repository=self.student_repo)

    def seed_data(self):

        u1 = User(
            username="testy",
            email="test@example.com",
            password="test",
            id="29a2ba2b-0db4-41bb-87b0-a5af98462a42",
        )
        self.user_repo.add(u1)

        u2 = User(
            username="loki",
            email="test2@example.com",
            password="test2",
            id="665fff20-adee-4e53-8b61-3c776b3e39a1",
        )
        self.user_repo.add(u2)

        s1 = Student(
            id="d7c5b248-ce66-4485-ac28-36d49149c2a1",
            name="Alice",
            email="test@example",
        )
        self.student_repo.add(s1)


auth_service = None
student_service = None

if ENVIRONMENT == "dev":
    dev_context = AppContext()
    dev_context.seed_data()

    auth_service = dev_context.auth_service
    student_service = dev_context.student_service
else:
    raise RuntimeError("Unknown environment", ENVIRONMENT)
