from sqlalchemy.orm import session

from app.entities.role_scope_entity import RoleScopeEntity
from app.entities.scope_entity import ScopeEntity
from app.entities.user_role_entity import UserRoleEntity
from app.log import logger


class UserScopeController:
    def __init__(self, db_session: session = None):
        self.db_session = db_session

    def get_user_scopes(self, user_id: str):
        """Get scopes assigned to a specified user"""

        user_roles = self.db_session.query(UserRoleEntity).filter_by(user_id=user_id).all()
        roles_id = [user_role.to_dict().get("role_id") for user_role in user_roles]

        user_scopes = self.db_session.query(RoleScopeEntity).filter(RoleScopeEntity.role_id.in_(roles_id)).all()
        scopes_id = [user_scope.to_dict().get("scope_id") for user_scope in user_scopes]

        scopes = self.db_session.query(ScopeEntity).filter(ScopeEntity.scope_id.in_(scopes_id)).all()

        return [scope.to_dict().get("name") for scope in scopes]
