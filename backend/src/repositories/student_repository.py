from typing import List, Optional
from src.domain.models import Student
from src.repositories.interfaces import Repository


class InMemoryStudentRepository(Repository):
    def __init__(self):
        self.students: List[Student] = []
        self.next_id = 0

    def get_all(self) -> List[Student]:
        return self.students.copy()

    def get_by_id(self, student_id: int) -> Optional[Student]:
        return next((s for s in self.students if s.id == student_id), None)

    def add(self, student: Student) -> Student:
        student.id = self.next_id
        self.next_id += 1
        self.students.append(student)
        return student


from typing import List, Optional
from google.cloud import firestore
from dataclasses import asdict

class FirebaseStudentRepository(Repository):
    def __init__(self, collection_name: str = "students"):
        # This assumes you have initialized the Firebase Admin SDK or 
        # have your GOOGLE_APPLICATION_CREDENTIALS environment variable set.
        self.db = firestore.Client()
        self.collection = self.db.collection(collection_name)

    def get_all(self) -> List[Student]:
        docs = self.collection.stream()
        return [Student(**doc.to_dict()) for doc in docs]

    def get_by_id(self, student_id: str) -> Optional[Student]:
        doc_ref = self.collection.document(student_id)
        doc = doc_ref.get()
        if doc.exists:
            return Student(**doc.to_dict())
        return None

    def add(self, student: Student) -> Student:
        # Convert dataclass to dictionary for Firestore storage
        student_data = asdict(student)
        # Use the student.id as the document ID
        self.collection.document(student.id).set(student_data)
        return student