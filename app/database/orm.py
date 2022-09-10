import logging
import uuid
from datetime import datetime

from sqlalchemy import Table, MetaData, Column, VARCHAR, DATE, BIGINT
from sqlalchemy.orm import mapper

from app.entities.role_entity import RoleEntity
from app.entities.role_scope_entity import RoleScopeEntity
from app.entities.scope_entity import ScopeEntity
from app.entities.user_role_entity import UserRoleEntity

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

role_scope = Table(
    "role_scope",
    metadata,
    Column("role_scope_id", BIGINT, primary_key=True, nullable=False, unique=True, autoincrement=True),
    Column("role_id", VARCHAR(36), nullable=False),
    Column("scope_id", VARCHAR(36), nullable=False),
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

scope = Table(
    "scope",
    metadata,
    Column("scope_id", VARCHAR(36), primary_key=True, nullable=False, unique=True, default=new_uuid),
    Column("name", VARCHAR(20), nullable=False, unique=True),
    Column("description", VARCHAR(200), nullable=False),
)


def start_mappers():
    logger.info("================> Starting mappers")
    mapper(UserRoleEntity, user_role)
    mapper(RoleScopeEntity, role_scope)
    mapper(RoleEntity, role)
    mapper(ScopeEntity, scope)
