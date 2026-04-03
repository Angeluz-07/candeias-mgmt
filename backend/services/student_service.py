from typing import List, Optional
from domain.models import Student
from repositories.interfaces import Repository

class StudentService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def get_all_students(self) -> List[Student]:
        return self.repository.get_all()

    def get_student_by_id(self, student_id: int) -> Optional[Student]:
        return self.repository.get_by_id(student_id)

    def add_student(self, name: str, email: str) -> Student:
        student = Student(id=None, name=name, email=email)
        return self.repository.add(student)