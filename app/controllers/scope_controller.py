from sqlalchemy.orm import session

from app.entities.scope_entity import ScopeEntity
from app.exceptions.exceptions import ScopeAlreadyExistsException, ScopeNotFoundException


class ScopeController:
    def __init__(self, db_session: session = None):
        self.db_session = db_session

    def get_scope_by_id(self, scope_id):
        """Get scope by scope id"""

        scope = self.db_session.query(ScopeEntity).filter_by(scope_id=scope_id).first()
        if not scope:
            raise ScopeNotFoundException(scope_id)

        return scope.to_dict()

    def get_scope_by_name(self, scope_name):
        """Get scope by scope name"""

        scope = self.db_session.query(ScopeEntity).filter_by(name=scope_name).first()
        if not scope:
            raise ScopeNotFoundException(scope_name)

        return scope.to_dict()

    def create_scope(self, new_scope: ScopeEntity):
        """Storage new_scope in database"""

        scope = self.db_session.query(ScopeEntity).filter_by(name=new_scope.name).first()
        if scope:
            raise ScopeAlreadyExistsException(scope.name)

        self.db_session.add(new_scope)
        self.db_session.commit()

        return new_scope.to_dict()
