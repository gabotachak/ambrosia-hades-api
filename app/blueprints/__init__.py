from app.blueprints.ping_views import ping_bp
from app.blueprints.role_scope_views import role_scope_bp
from app.blueprints.role_views import role_bp
from app.blueprints.scope_views import scope_bp
from app.blueprints.user_role_views import user_role_bp
from app.blueprints.user_scope_views import user_scope_bp

__all__ = ["ping_bp", "role_scope_bp", "role_bp", "scope_bp", "user_role_bp", "user_scope_bp"]
