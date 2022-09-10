from sqlalchemy.orm import session

from app.entities.role_entity import RoleEntity
from app.entities.user_role_entity import UserRoleEntity
from app.exceptions.exceptions import UserRolesNotFoundException
from app.utils.constants import ROLES


class UserRoleController:
    def __init__(self, db_session: session = None):
        self.db_session = db_session

    def get_user_roles(self, user_id: str):
        """Get roles assigned to a specified user"""

        roles = self.db_session.query(RoleEntity).filter(
            UserRoleEntity.user_id == user_id,
            UserRoleEntity.role_id == RoleEntity.role_id
        ).all()

        if len(roles) == 0:
            raise UserRolesNotFoundException(user_id)

        return [role.name for role in roles]

    def add_roles_to_user(self, user_id: str, roles_list):
        """Add roles to a specified user by id"""

        roles_to_assign = self.db_session.query(RoleEntity).filter(RoleEntity.name.in_(roles_list)).all()

        try:
            old_roles = self.get_user_roles(user_id)
        except UserRolesNotFoundException:
            old_roles = []

        for role in roles_to_assign:
            if role.name not in old_roles:
                user_role = UserRoleEntity(
                    user_id=user_id,
                    role_id=role.role_id,
                    role_name=role.name
                )
                self.db_session.add(user_role)

        self.db_session.commit()

        try:
            actual_roles = self.get_user_roles(user_id)
        except UserRolesNotFoundException:
            actual_roles = []

        return {ROLES: actual_roles}

    def set_roles_in_user(self, user_id: str, roles_list):
        """Set roles in a specified user by id"""

        self.db_session.query(UserRoleEntity).filter(UserRoleEntity.user_id == user_id).delete()

        return self.add_roles_to_user(user_id, roles_list)
