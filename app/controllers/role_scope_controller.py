from sqlalchemy.orm import session

from app.entities.role_entity import RoleEntity
from app.entities.role_scope_entity import RoleScopeEntity
from app.entities.scope_entity import ScopeEntity
from app.exceptions.exceptions import RoleScopesNotFoundException, RoleNotFoundException


class RoleScopeController:
    def __init__(self, db_session: session = None):
        self.db_session = db_session

    def _get_role_scopes(self, role: RoleEntity):
        """Get scopes assigned to a specified role"""

        scopes = self.db_session.query(ScopeEntity).filter(
            RoleScopeEntity.scope_id == ScopeEntity.scope_id,
            RoleScopeEntity.role_id == role.role_id
        ).all()

        if len(scopes) == 0:
            raise RoleScopesNotFoundException(role.name)

        return [scope.name for scope in scopes]

    def get_role_scopes_by_id(self, role_id: str):
        role = self.db_session.query(RoleEntity).filter_by(role_id=role_id).first()
        if not role:
            raise RoleNotFoundException(role_id)

        return self._get_role_scopes(role)

    def get_role_scopes_by_name(self, role_name: str):
        role = self.db_session.query(RoleEntity).filter_by(name=role_name).first()
        if not role:
            raise RoleNotFoundException(role_name)

        return self._get_role_scopes(role)
