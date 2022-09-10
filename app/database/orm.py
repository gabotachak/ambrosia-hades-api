import logging
import uuid
from datetime import datetime

from sqlalchemy import Table, MetaData, Column, VARCHAR, ForeignKeyConstraint, DATETIME
from sqlalchemy.orm import mapper

from app.entities.role_entity import RoleEntity
from app.entities.role_scope_entity import RoleScopeEntity
from app.entities.scope_entity import ScopeEntity
from app.entities.user_role_entity import UserRoleEntity

logger = logging.getLogger(__name__)

metadata = MetaData()


def new_uuid() -> str:
    return str(uuid.uuid4())


role = Table(
    "role",
    metadata,
    Column("role_id", VARCHAR(36), primary_key=True, nullable=False, unique=True, default=new_uuid),
    Column("name", VARCHAR(20), nullable=False, unique=True),
    Column("description", VARCHAR(200), nullable=False)
)

scope = Table(
    "scope",
    metadata,
    Column("scope_id", VARCHAR(36), primary_key=True, nullable=False, unique=True, default=new_uuid),
    Column("name", VARCHAR(20), nullable=False, unique=True),
    Column("description", VARCHAR(200), nullable=False)
)

role_scope = Table(
    "role_scope",
    metadata,
    Column("role_id", VARCHAR(36), primary_key=True, nullable=False),
    Column("role_name", VARCHAR(20), primary_key=True, nullable=False),
    Column("scope_id", VARCHAR(36), primary_key=True, nullable=False),
    Column("scope_name", VARCHAR(20), primary_key=True, nullable=False),
    Column("assign_date", DATETIME, nullable=False, default=datetime.now),
    Column("assign_status", VARCHAR(10), nullable=False, default="ACTIVE"),
    ForeignKeyConstraint(('role_id', 'role_name'), ('role.role_id', 'role.name')),
    ForeignKeyConstraint(('scope_id', 'scope_name'), ('scope.scope_id', 'scope.name'))
)

user_role = Table(
    "user_role",
    metadata,
    Column("user_id", VARCHAR(36), primary_key=True, nullable=False),
    Column("role_id", VARCHAR(36), primary_key=True, nullable=False),
    Column("role_name", VARCHAR(20), primary_key=True, nullable=False),
    Column("assign_date", DATETIME, nullable=False, default=datetime.now),
    Column("assign_status", VARCHAR(10), nullable=False, default="ACTIVE"),
    ForeignKeyConstraint(('role_id', 'role_name'), ('role.role_id', 'role.name'))
)


def start_mappers():
    logger.info("================> Starting mappers")
    mapper(UserRoleEntity, user_role)
    mapper(RoleScopeEntity, role_scope)
    mapper(RoleEntity, role)
    mapper(ScopeEntity, scope)
