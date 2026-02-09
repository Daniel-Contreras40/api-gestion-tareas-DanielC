from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base


# Tabla puente Task <-> Project (N-N)
task_project = Table(
    "task_project",
    Base.metadata,
    Column("task_id", Integer, ForeignKey("tasks.id")),
    Column("project_id", Integer, ForeignKey("projects.id"))
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    tasks = relationship("Task", back_populates="owner")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(String(255))

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    tasks = relationship("Task", secondary=task_project, back_populates="projects")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(String(255))
    due_date = Column(Date)
    status = Column(String(20), default="pending")

    owner_id = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    owner = relationship("User", back_populates="tasks")
    projects = relationship("Project", secondary=task_project, back_populates="tasks")