from fastapi import APIRouter, HTTPException
from typing import List
from domain.models import Student
from entrypoints.context import student_service

router = APIRouter()

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


from pydantic import EmailStr
from pydantic import BaseModel
from fastapi import status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from services.auth_service import auth_backend
from entrypoints.context import auth_service


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


security = HTTPBearer()


@router.post("/login")
def login(login_schema: LoginRequest):
    authorized = auth_service.is_user_authorized(
        login_schema.email, login_schema.password
    )

    if not authorized:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas"
        )

    user = auth_service.get_user_by_email(login_schema.email)
    # AuthX genera el token usando el ID del usuario
    token = auth_backend.create_access_token(uid=user.id)
    return {"access_token": token, "token_type": "bearer"}


# 5. Ruta Protegida
@router.get("/me")
def get_current_user(
    token: HTTPAuthorizationCredentials = Depends(security),
    payload=Depends(auth_backend.access_token_required),
):
    user_id = payload.sub
    user = auth_service.get_user_by_id(user_id)
    return {"username": user.username, "email": user.email, "id": user.id}
