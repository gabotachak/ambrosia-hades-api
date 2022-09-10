from sqlalchemy.orm import session


class RoleScopeController:
    def __init__(self, db_session: session = None):
        self.db_session = db_session
