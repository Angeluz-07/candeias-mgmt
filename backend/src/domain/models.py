from dataclasses import dataclass, field
from typing import Optional
from uuid import uuid4

@dataclass
class User:
    username: str
    email: str
    password: str
    id: str = field(default_factory=lambda: str(uuid4()))

@dataclass
class Student:
    name: str
    email: str
    id: str = field(default_factory=lambda: str(uuid4()))


@dataclass
class PaymentInfo:
    student_id: str
    is_paid: bool
    id: str = field(default_factory=lambda: str(uuid4()))
