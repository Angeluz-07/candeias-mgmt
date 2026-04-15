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

import os
from pymongo import MongoClient
from typing import List, Optional
from config import MONGODB_CONN_STR, MONGODB_DB_NAME, ENVIRONMENT
from pymongo.errors import DuplicateKeyError

class CosmosStudentRepository:
    def __init__(self):
        allow_invalid_ssl = ENVIRONMENT == "dev"
        # Usamos la configuración que ya validamos para el emulador
        self.client = MongoClient(
            MONGODB_CONN_STR,
            retryWrites=False,
            tlsAllowInvalidCertificates=allow_invalid_ssl
        )
        self.db = self.client[MONGODB_DB_NAME]
        self.collection = self.db["students"]

    def _map_to_student(self, data: dict) -> Optional[Student]:
        """Convierte el documento de Mongo al objeto de dominio Student"""
        if not data:
            return None
        
        # Mapeamos el _id de Mongo de vuelta al atributo id del objeto
        data['id'] = str(data.pop('_id'))
        return Student(**data)

    def get_all(self) -> List[Student]:
        # Buscamos todos y convertimos a objetos Student
        cursor = self.collection.find({})
        return [self._map_to_student(s) for s in cursor]

    def get_by_id(self, student_id: str) -> Optional[Student]:
        # En el API de Mongo, buscamos por la clave primaria _id
        data = self.collection.find_one({"_id": student_id})
        return self._map_to_student(data)

    def add(self, student: Student) -> Student:
        # Convertimos el objeto a diccionario para Mongo
        student_data = student.__dict__.copy()
        
        # Como el objeto ya trae un UUID en 'id', lo asignamos a '_id'
        student_data['_id'] = student_data.pop('id')
    

        try:
            self.collection.insert_one(student_data)
            #print(f"✅ Estudiante {student.id} insertado.")
        except DuplicateKeyError:
            print(f"⚠️ {student_data['_id']} ya existe. Skip")

        return student