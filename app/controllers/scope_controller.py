from sqlalchemy.orm import session

from app.entities.scope_entity import ScopeEntity
from app.exceptions.exceptions import ScopeAlreadyExistsException


class ScopeController:
    def __init__(self, db_session: session = None):
        self.db_session = db_session

    def create_scope(self, new_scope: ScopeEntity):
        """Storage new_scope in database"""

        scope = self.db_session.query(ScopeEntity).filter_by(name=new_scope.name).first()
        if scope:
            raise ScopeAlreadyExistsException(scope.name)

        self.db_session.add(new_scope)
        self.db_session.commit()

        return new_scope.to_dict()
