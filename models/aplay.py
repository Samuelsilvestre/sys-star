from src.settins.dbconnection import Dbconnection
from src.settins.base import Base
from src.models.sys_star import SysStar

def aplay():
    db = Dbconnection()
    Base.metadata.create_all(db.engine)

    