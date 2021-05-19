from src.dao.register_user_dao import RegisterUserDao

class RegisterUserController:

    def create_register(self, register_name, register_last_name, register_user, register_password):
        if type(register_name, register_last_name, register_user, register_password) == str:
            register = {
                'name' : register_name,
                'last_name' : register_last_name,
                'user' : register_user,
                'password' : register_password
            }
            register_id = RegisterUserDao(register).create()
            return register_id
        raise Exception('Valor invalido!')

    def read_all(self):
        register = RegisterUserDao().read_all()
        return register

    def read_by_id(self, register_id):
        register = {
            'id': register_id
        }
        register_user = RegisterUserDao(register).read_by_id()
        return register_user
    
    def update(self, register_id, register_name, register_last_name, register_user, register_password):
        register_update = {
            'id': register_id,
            'name' : register_name,
            'last_name' : register_last_name,
            'user' : register_user,
            'password' : register_password
        }
        RegisterUserDao(register_update).update()