from src.models.sys_star import SysStar
from src.settins.base_session import SessionBase

class GetObject:

    def get_all(self):
        session_base = SessionBase()
        object = session_base.session.query(SysStar)
        return object


