from sqlalchemy.orm import session

from app.entities.role_entity import RoleEntity
from app.entities.user_role_entity import UserRoleEntity


class UserRoleController:
    def __init__(self, db_session: session = None):
        self.db_session = db_session

    def get_user_roles(self, user_id: str):
        """Get roles assigned to a specified user"""

        roles = self.db_session.query(RoleEntity).filter(
            UserRoleEntity.user_id == user_id,
            UserRoleEntity.role_id == RoleEntity.role_id
        ).all()

        return [role.name for role in roles]
