from src.settins.base import Base
from sqlalchemy import Column, String, Integer, Float, BLOB


class SysStar(Base):
    __tablename__ = 'sys_star'
    id = Column(Integer, primary_key = True)
    name_system = Column(String(200), index = True, unique = True)
    light_years = Column(Float, index = True)
    image = Column(BLOB)

    def __repr__(self):
        return  {'name_system': self.name_system}