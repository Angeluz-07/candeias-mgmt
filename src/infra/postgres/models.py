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
    duration = Column(Integer, nullable=False)
    cost = Column(Float, nullable=False)
    gym_id = Column(String, ForeignKey("gyms.id"), nullable=False)
    member_id = Column(String, ForeignKey("members.id"), nullable=False)

    gym = relationship("GymBase")
    member = relationship("MemberBase")
