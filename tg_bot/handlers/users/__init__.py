from .admin import register_admin_hanlers
from .echo import register_echo_handler
from .start import register_start_handlers


def register_users_handlers(dp):
    register_admin_hanlers(dp)
    register_start_handlers(dp)
    
    register_echo_handler(dp)


__all__ = ["register_users_handlers"]
