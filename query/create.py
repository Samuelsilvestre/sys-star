import base64
from src.models.sys_star import *
from src.settins.base_session import SessionBase


class CreateSystar:

    def encode(self, dir):
        with open(dir, 'rb') as image:
            encode_image = base64.b64encode(image.read())
        return encode_image

    def insert(self, name_system: str, light_years: float, image: any):
        new = SysStar(name_system = name_system, light_years = light_years, image = image)
        session_base = SessionBase()
        session_base.session.add(new)
        session_base.session.commit()
