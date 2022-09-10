from sqlalchemy.orm import session

from app.entities.role import RoleEntity
from app.entities.user_role import UserRoleEntity


class UserRoleController:
    def __init__(self, db_session: session = None):
        self.db_session = db_session

    def get_user_roles(self, user_id: str):
        """Get roles assigned to a specified user"""

        user_roles = self.db_session.query(UserRoleEntity).filter_by(user_id=user_id).all()

        roles_id = [user_role.to_dict().get("role_id") for user_role in user_roles]
        roles = self.db_session.query(RoleEntity).filter(RoleEntity.role_id.in_(roles_id)).all()

        return [role.to_dict().get("name") for role in roles]
