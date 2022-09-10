from sqlalchemy.orm import session

from app.entities.role_scope_entity import RoleScopeEntity
from app.entities.scope_entity import ScopeEntity
from app.exceptions.exceptions import RoleScopesNotFoundException


class RoleScopeController:
    def __init__(self, db_session: session = None):
        self.db_session = db_session

    def get_role_scopes(self, role_id: str):
        """Get scopes assigned to a specified role"""

        scopes = self.db_session.query(ScopeEntity).filter(
            RoleScopeEntity.scope_id == ScopeEntity.scope_id,
            RoleScopeEntity.role_id == role_id
        ).all()

        if len(scopes) == 0:
            raise RoleScopesNotFoundException(role_id)

        return [scope.name for scope in scopes]
