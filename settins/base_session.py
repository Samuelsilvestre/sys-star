from sqlalchemy.orm.session import Session
from src.settins.dbconnection import Dbconnection

### SessionBase ###
class SessionBase(Dbconnection):

    def __init__(self):
        self.session = self.__open_session()
    
    def __open_session(self) -> Session:
        with Dbconnection() as db:
            return db.session