from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass
class Member:
    name: str
    email: str
    phone: str
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class Gym:
    name: str
    id: str = field(default_factory=lambda: str(uuid4()))


@dataclass
class Membership:
    duration: int
    cost: float
    gym_id: str
    member_id: str
    id: str = field(default_factory=lambda: str(uuid4()))


@dataclass
class Owner:
    name: str
    email: str
    phone: str
    gym_id: str
    id: str = field(default_factory=lambda: str(uuid4()))
