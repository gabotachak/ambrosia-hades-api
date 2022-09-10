from sqlalchemy.orm import session

from app.entities.role_entity import RoleEntity
from app.exceptions.exceptions import RoleAlreadyExistsException


class RoleController:
    def __init__(self, db_session: session = None):
        self.db_session = db_session

    def create_role(self, new_role: RoleEntity):
        """Storage new_role in database"""

        role = self.db_session.query(RoleEntity).filter_by(name=new_role.name).first()
        if role:
            raise RoleAlreadyExistsException(role.name)

        self.db_session.add(new_role)
        self.db_session.commit()

        return new_role.to_dict()
