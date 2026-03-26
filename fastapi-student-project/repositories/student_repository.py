from abc import ABC, abstractmethod
from typing import List, Optional
from domain.student import Student

class StudentRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Student]:
        pass

    @abstractmethod
    def get_by_id(self, student_id: int) -> Optional[Student]:
        pass

    @abstractmethod
    def add(self, student: Student) -> Student:
        pass

class InMemoryStudentRepository(StudentRepository):
    def __init__(self):
        self.students: List[Student] = []
        self.next_id = 1

    def get_all(self) -> List[Student]:
        return self.students.copy()

    def get_by_id(self, student_id: int) -> Optional[Student]:
        return next((s for s in self.students if s.id == student_id), None)

    def add(self, student: Student) -> Student:
        student.id = self.next_id
        self.next_id += 1
        self.students.append(student)
        return student