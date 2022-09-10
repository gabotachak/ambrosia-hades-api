from sqlalchemy.orm import session

from app.entities.role_scope_entity import RoleScopeEntity
from app.entities.scope_entity import ScopeEntity
from app.entities.user_role_entity import UserRoleEntity


class UserScopeController:
    def __init__(self, db_session: session = None):
        self.db_session = db_session

    def get_user_scopes(self, user_id: str):
        """Get scopes assigned to a specified user"""

        user_roles = self.db_session.query(UserRoleEntity).filter_by(user_id=user_id).all()
        roles_id = [user_role.role_id for user_role in user_roles]

        scopes = self.db_session.query(ScopeEntity).filter(
            RoleScopeEntity.scope_id == ScopeEntity.scope_id,
            RoleScopeEntity.role_id.in_(roles_id)
        ).all()

        return [scope.name for scope in scopes]
