from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

### Dbconnection ###
class Dbconnection:
    ''''connection database'''
    def __init__(self):
        self.string = config('DB')
        self.engine = self.__engine()
        self.session = None

    def __engine(self):
        engine = create_engine(self.string, echo = True)
        return engine
    
    def __enter__(self):
        session_maker = sessionmaker(bind = self.engine)
        self.session = session_maker()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()