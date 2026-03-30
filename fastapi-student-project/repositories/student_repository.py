from typing import List, Optional
from domain.student import Student
from repositories.interfaces import Repository

class InMemoryStudentRepository(Repository):
    def __init__(self):
        self.students: List[Student] = [
            Student(id=1, name="Alice", email="test@example")
        ]
        self.next_id = 2

    def get_all(self) -> List[Student]:
        return self.students.copy()

    def get_by_id(self, student_id: int) -> Optional[Student]:
        return next((s for s in self.students if s.id == student_id), None)

    def add(self, student: Student) -> Student:
        student.id = self.next_id
        self.next_id += 1
        self.students.append(student)
        return student
