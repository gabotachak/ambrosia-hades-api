import logging
import uuid
from datetime import datetime

from sqlalchemy import Table, MetaData, Column, VARCHAR, DATE, BIGINT
from sqlalchemy.orm import mapper

from app.entities.role import RoleEntity
from app.entities.user_role import UserRoleEntity

logger = logging.getLogger(__name__)

metadata = MetaData()


def new_uuid() -> str:
    return str(uuid.uuid4())


user_role = Table(
    "user_role",
    metadata,
    Column("user_role_id", BIGINT, primary_key=True, nullable=False, unique=True, autoincrement=True),
    Column("user_id", VARCHAR(36), nullable=False),
    Column("role_id", VARCHAR(36), nullable=False),
    Column("assign_date", DATE, default=datetime.now),
    Column("assign_status", VARCHAR(10), default="ACTIVE"),
)

role = Table(
    "role",
    metadata,
    Column("role_id", VARCHAR(36), primary_key=True, nullable=False, unique=True, default=new_uuid),
    Column("name", VARCHAR(20), nullable=False, unique=True),
    Column("description", VARCHAR(200), nullable=False),
)


def start_mappers():
    logger.info("================> Starting mappers")
    mapper(UserRoleEntity, user_role)
    mapper(RoleEntity, role)
