from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from uuid import uuid4
from dateutil.relativedelta import relativedelta


@dataclass
class Gym:
    name: str
    id: str = field(default_factory=lambda: str(uuid4()))


@dataclass
class Membership:
    start_date: datetime
    due_date: datetime
    expires_at: datetime
    cost: float

    gym_id: str
    member_id: str
    id: str = field(default_factory=lambda: str(uuid4()))

    @property
    def status(self) -> dict:
        today = date.today()

        if today <= self.expires_at:
            return {
                "status": "ACTIVE",
                "label": "🟢 Al día",
                "days_overdue": 0,
                "expires_at": self.membership.expires_at,
            }
        else:
            days_overdue = (today - self.membership.expires_at).days
            return {
                "status": "OVERDUE",
                "label": "🔴 En mora",
                "days_overdue": days_overdue,
                "expires_at": self.membership.expires_at,
            }


@dataclass
class Member:
    name: str
    email: str
    phone: str
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    membership: Membership = None


@dataclass
class Owner:
    name: str
    email: str
    phone: str
    gym_id: str
    id: str = field(default_factory=lambda: str(uuid4()))
