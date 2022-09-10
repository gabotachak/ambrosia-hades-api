from sqlalchemy.orm import session

from app.entities.role_scope_entity import RoleScopeEntity
from app.entities.scope_entity import ScopeEntity


class RoleScopeController:
    def __init__(self, db_session: session = None):
        self.db_session = db_session

    def get_role_scopes(self, role_id: str):
        """Get scopes assigned to a specified role"""

        role_scopes = self.db_session.query(RoleScopeEntity).filter_by(role_id=role_id).all()
        scopes_id = [role_scope.to_dict().get("scope_id") for role_scope in role_scopes]

        scopes = self.db_session.query(ScopeEntity).filter(ScopeEntity.scope_id.in_(scopes_id)).all()

        return [scope.to_dict().get("name") for scope in scopes]
