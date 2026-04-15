from src.domain.models import User
from src.repositories.interfaces import Repository


class InMemoryUserRepository(Repository):

    def __init__(self):
        self.items = []

    def get_all(self):
        return self.items

    def add(self, item: User):
        self.items.append(item)

    def get_by_id(self, id: str):
        return next((u for u in self.items if u.id == id), None)

    def get_by_email(self, email: str):
        return next((u for u in self.items if u.email == email), None)

import os
from pymongo import MongoClient
from typing import List, Optional
from config import MONGODB_CONN_STR, MONGODB_DB_NAME, ENVIRONMENT
from pymongo.errors import DuplicateKeyError

class CosmosUserRepository:
    def __init__(self):
        allow_invalid_ssl = ENVIRONMENT == "dev"
        # 1. Conexión usando variables de entorno
        self.client = MongoClient(
            MONGODB_CONN_STR,
            retryWrites=False, # fix to avoid default mongodb behaviour of retrywrites
            tlsAllowInvalidCertificates=allow_invalid_ssl
        )
        self.db = self.client[MONGODB_DB_NAME]
        self.collection = self.db["users"]

        # CONFIGURACIÓN EXPLÍCITA
        try:
            # 1. Forzamos la creación de la DB y la colección si no existen
            # En Cosmos DB (API Mongo), esto asegura que se asigne el rendimiento (RUs)
            if "users" not in self.db.list_collection_names():
                self.db.create_collection("users")
                print("Colección 'users' creada exitosamente.")

            # 2. CREACIÓN DE ÍNDICES (Vital para rendimiento)
            # Esto también asegura que la colección exista físicamente
            self.collection.create_index("email", unique=True)

        except Exception as e:
            print(f"Nota: La base de datos ya está inicializada o hubo un error: {e}")

    def _map_to_user(self, data: dict) -> Optional[User]:
        """Helper para convertir el dict de Mongo a tu objeto User"""
        if not data:
            return None
        # Asumiendo que User acepta los campos en el constructor
        # Importante: Mongo usa '_id', lo mapeamos al 'id' de tu objeto
        data["id"] = str(data.pop("_id"))
        return User(**data)

    def get_all(self) -> List[User]:
        cursor = self.collection.find({})
        return [self._map_to_user(u) for u in cursor]

    def add(self, user: User):
        # Convertimos el objeto User a diccionario
        user_dict = user.__dict__.copy()

        # Mongo usa _id, si tu User ya tiene id, lo renombramos
        if "id" in user_dict:
            user_dict["_id"] = user_dict.pop("id")
    
        try:
            self.collection.insert_one(user_dict)
            #print(f"✅ Estudiante {student.id} insertado.")
        except DuplicateKeyError:
            print(f"⚠️ {user_dict['_id']} ya existe. Skip")
        
    def get_by_id(self, user_id: str) -> Optional[User]:
        # Buscamos por el _id de Mongo
        data = self.collection.find_one({"_id": user_id})
        return self._map_to_user(data)

    def get_by_email(self, email: str) -> Optional[User]:
        data = self.collection.find_one({"email": email})
        return self._map_to_user(data)
