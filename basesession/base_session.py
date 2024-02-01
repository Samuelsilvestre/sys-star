from src.settins.dbconnection import Dbconnection
from sqlalchemy.orm import session

### Basession ###
class BaseSession:

    def objects(self) -> session:
        with Dbconnection() as db:
            return db.session