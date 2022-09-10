from sqlalchemy.orm import session

from app.entities.role_entity import RoleEntity
from app.entities.role_scope_entity import RoleScopeEntity
from app.entities.scope_entity import ScopeEntity
from app.exceptions.exceptions import RoleAlreadyExistsException, RoleNotFoundException


class RoleController:
    def __init__(self, db_session: session = None):
        self.db_session = db_session

    def get_role_by_name(self, role_name):
        role = self.db_session.query(RoleEntity).filter_by(name=role_name).first()
        if not role:
            raise RoleNotFoundException(role_name)

        role_scopes = self.db_session.query(RoleScopeEntity).filter_by(role_id=role.role_id).all()
        scopes_id = [role_scope.to_dict().get("scope_id") for role_scope in role_scopes]

        scopes = self.db_session.query(ScopeEntity).filter(ScopeEntity.scope_id.in_(scopes_id)).all()

        role_dict = role.to_dict()
        role_dict['scopes'] = [scope.to_dict().get("name") for scope in scopes]
        return role_dict

    def create_role(self, new_role: RoleEntity, scope_req=None):
        """Storage new_role in database"""

        role = self.db_session.query(RoleEntity).filter_by(name=new_role.name).first()
        if role:
            raise RoleAlreadyExistsException(role.name)

        self.db_session.add(new_role)

        if scope_req:
            scopes_to_assign = self.db_session.query(ScopeEntity).filter(ScopeEntity.name.in_(scope_req)).all()
            for scope in scopes_to_assign:
                role_scope = RoleScopeEntity(role_id=new_role.role_id, scope_id=scope.scope_id)
                self.db_session.add(role_scope)

        self.db_session.commit()

        return new_role.to_dict()
