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


from typing import List, Optional
from google.cloud import firestore
from dataclasses import asdict


class FirebaseUserRepository(Repository):
    def __init__(self, collection_name: str = "users"):
        self.db = firestore.Client()
        self.collection = self.db.collection(collection_name)

    def get_all(self) -> List[User]:
        docs = self.collection.stream()
        return [User(**doc.to_dict()) for doc in docs]

    def add(self, user: User) -> User:
        user_data = asdict(user)
        # We use the user's UUID as the document ID
        self.collection.document(user.id).set(user_data)
        return user

    def get_by_id(self, user_id: str) -> Optional[User]:
        doc = self.collection.document(user_id).get()
        if doc.exists:
            return User(**doc.to_dict())
        return None

    def get_by_email(self, email: str) -> Optional[User]:
        # Firestore query to find a user where the email field matches
        query = self.collection.where("email", "==", email).limit(1).stream()

        for doc in query:
            return User(**doc.to_dict())
        return None
