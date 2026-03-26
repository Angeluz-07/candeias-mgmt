from fastapi import APIRouter, HTTPException
from typing import List
from domain.student import Student
from services.student_service import StudentService

router = APIRouter()

def get_student_service() -> StudentService:
    # In a real app, this would be dependency injection
    from repositories.student_repository import InMemoryStudentRepository
    repo = InMemoryStudentRepository()
    return StudentService(repo)

student_service = get_student_service()

@router.get("/students", response_model=List[Student])
def get_students():
    return student_service.get_all_students()

@router.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    student = student_service.get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.post("/students", response_model=Student)
def create_student(student: Student):
    return student_service.add_student(student.name, student.email)