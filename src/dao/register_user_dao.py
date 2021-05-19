from config.database import Database
from src.model.register_user_model import RegisterUserModel

class RegisterUserDao:

        def __init__(self, register:dict={}, first_create=False):
            self.register = register
            self.__autocreate() if first_create else None

        def create(self):

            with Database() as session:
                register = RegisterUserModel(
                    name = self.register['name'],
                    last_name = self.register['last_name'],
                    user = self.register['user'],
                    password = self.register['password']
                )
                session.add(register)
                session.flush()
                session.commit()
                return register.id
            
        def read_all(self):

            with Database() as session:
                result = session.query(RegisterUserModel).all()
                return result

        def read_by_id(self):
            with Database() as session:
                result = session.query(RegisterUserModel).filter_by(id=self.register['id']).all()
                return result[0]

        def update(self):

            if not 'id' in self.register or not self.register['id']:
                return self.create()
            with Database() as session:
                register_update = session.query(RegisterUserModel).filter_by(id=self.register['id'])
                register_update.update({
                    'id': self.register['id'],
                    'name': self.register['name'] if self.register['name'] else register_update[0].name,
                    'last_name': self.register['last_name'] if self.register['last_name'] else register_update[0].last_name,
                    'user': self.register['user'] if self.register['user'] else register_update[0].user,
                    'password': self.register['password'] if self.register['password'] else register_update[0].password,
                })
                session.commit()