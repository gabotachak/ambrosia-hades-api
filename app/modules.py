import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.controllers.role_controller import RoleController
from app.controllers.role_scope_controller import RoleScopeController
from app.controllers.scope_controller import ScopeController
from app.controllers.user_role_controller import UserRoleController
from app.controllers.user_scope_controller import UserScopeController


def new_session_factory():
    load_dotenv()

    db_host = os.getenv("DB_HOST", "")
    db_port = os.getenv("DB_PORT", "")
    db_schema = os.getenv("DB_SCHEMA", "")
    db_user = os.getenv("DB_USER", "")
    db_password = os.getenv("DB_PASSWORD", "")

    uri = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_schema}"

    return sessionmaker(bind=create_engine(uri))


session_factory = new_session_factory()
db_session = session_factory()

role_scope_controller = RoleScopeController(db_session=db_session)
role_controller = RoleController(db_session=db_session)
scope_controller = ScopeController(db_session=db_session)
user_role_controller = UserRoleController(db_session=db_session)
user_scope_controller = UserScopeController(db_session=db_session)
