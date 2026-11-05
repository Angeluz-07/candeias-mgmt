from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    Boolean,
    Date,
    or_,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from src.infra.postgres.repo import Base


class MemberBase(Base):
    """
    Defines the table structure in db
    """

    __tablename__ = "members"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    created_at = Column(Date, nullable=False)

    membership = relationship("MembershipBase", back_populates="member", uselist=False, cascade="all, delete-orphan")

class GymBase(Base):
    """
    Defines the table structure in db
    """

    __tablename__ = "gyms"

    # In SQL, the primary key (id) is typically an auto-incrementing integer.
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)


class MembershipBase(Base):
    """
    Defines the table structure in db
    """

    __tablename__ = "memberships"

    # In SQL, the primary key (id) is typically an auto-incrementing integer.
    id = Column(String, primary_key=True, index=True)
    gym_id = Column(String, ForeignKey("gyms.id"), nullable=False)
    member_id = Column(String, ForeignKey("members.id"), nullable=False)

    start_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)       # Día límite de pago fijo (ej. el 5)
    expires_at = Column(Date, nullable=False)     # Fin de cobertura
    cost = Column(Float, nullable=False)

    gym = relationship("GymBase")
    member = relationship("MemberBase", back_populates="membership")
