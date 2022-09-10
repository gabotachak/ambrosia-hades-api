from sqlalchemy.orm import session

from app.entities.role_entity import RoleEntity
from app.entities.role_scope_entity import RoleScopeEntity
from app.entities.scope_entity import ScopeEntity
from app.exceptions.exceptions import RoleScopesNotFoundException, RoleNotFoundException
from app.utils.constants import SCOPES


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
        """Get scopes assigned to a specified role by id"""

        role = self.db_session.query(RoleEntity).filter_by(role_id=role_id).first()
        if not role:
            raise RoleNotFoundException(role_id)

        return self._get_role_scopes(role)

    def get_role_scopes_by_name(self, role_name: str):
        """Get scopes assigned to a specified role by name"""

        role = self.db_session.query(RoleEntity).filter_by(name=role_name).first()
        if not role:
            raise RoleNotFoundException(role_name)

        return self._get_role_scopes(role)

    def _add_scopes_to_role(self, role: RoleEntity, scopes_list):
        """Add scopes to a specified role"""

        scopes_to_assign = self.db_session.query(ScopeEntity).filter(ScopeEntity.name.in_(scopes_list)).all()
        old_scopes = self._get_role_scopes(role)

        for scope in scopes_to_assign:
            if scope.name not in old_scopes:
                role_scope = RoleScopeEntity(
                    role_id=role.role_id,
                    role_name=role.name,
                    scope_id=scope.scope_id,
                    scope_name=scope.name
                )
                self.db_session.add(role_scope)

        self.db_session.commit()

        role_dict = role.to_dict()

        try:
            role_dict[SCOPES] = self._get_role_scopes(role)
        except RoleScopesNotFoundException:
            role_dict[SCOPES] = []

        return role_dict

    def add_scopes_to_role_by_id(self, role_id: str, scopes_list):
        """Add scopes to a specified role by id"""

        role = self.db_session.query(RoleEntity).filter_by(role_id=role_id).first()
        if not role:
            raise RoleNotFoundException(role_id)

        return self._add_scopes_to_role(role, scopes_list)

    def add_scopes_to_role_by_name(self, role_name: str, scopes_list):
        """Add scopes to a specified role by name"""

        role = self.db_session.query(RoleEntity).filter_by(name=role_name).first()
        if not role:
            raise RoleNotFoundException(role_name)

        return self._add_scopes_to_role(role, scopes_list)

    def _set_scopes_in_role(self, role: RoleEntity, scopes_list):
        """Set scopes in a specified role"""

        self.db_session.query(RoleScopeEntity).filter(RoleScopeEntity.role_id == role.role_id).delete()

        return self._add_scopes_to_role(role, scopes_list)

    def set_scopes_in_role_by_id(self, role_id: str, scopes_list):
        """Set scopes in a specified role by id"""

        role = self.db_session.query(RoleEntity).filter_by(role_id=role_id).first()
        if not role:
            raise RoleNotFoundException(role_id)

        return self._set_scopes_in_role(role, scopes_list)

    def set_scopes_in_role_by_name(self, role_name: str, scopes_list):
        """Set scopes in a specified role by name"""

        role = self.db_session.query(RoleEntity).filter_by(name=role_name).first()
        if not role:
            raise RoleNotFoundException(role_name)

        return self._set_scopes_in_role(role, scopes_list)
