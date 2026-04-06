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
    