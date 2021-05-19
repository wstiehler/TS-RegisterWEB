from sqlalchemy import Column, Integer, String
from config.settings import Settings

class RegisterUserModel(Settings.Base):

    __tablename__ = 'register_user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)
    user = Column(String)
    password = Column(String)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.last_name} - {self.user} - {self.password}'