from authx import AuthX, AuthXConfig
from pwdlib import PasswordHash
from domain.models import User
from repositories.interfaces import Repository

# 1. Configuración de Seguridad
password_helper = PasswordHash.recommended()

config = AuthXConfig(
    JWT_SECRET_KEY="SUPER_SECRET",  # Usa una clave real en prod
    JWT_ACCESS_COOKIE_NAME="access_token",
    JWT_TOKEN_LOCATION=["headers"],
)

auth_backend = AuthX(config=config)


class AuthService:
    def __init__(self, user_repository: Repository):
        self.user_repository = user_repository

    def is_user_authorized(self, email, password):
        user = self.user_repository.get_by_email(email)
        # if not user or not password_helper.verify(credentials.password, user.password):
        return user and user.password == password

    def get_user_by_email(self, email):
        return self.user_repository.get_by_email(email)

    def get_user_by_id(self, user_id):
        return self.user_repository.get_by_id(user_id)


def get_auth_service():
    from repositories.user_repository import InMemoryUserRepository

    auth_service = AuthService(user_repository=InMemoryUserRepository())
    return auth_service


auth_service = get_auth_service()
