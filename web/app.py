from flask import Flask, render_template
import sys, os
sys.path.append(os.getcwd())
from src.controller.register_user_controller import RegisterUserController


app = Flask(__name__)

app.route('/')
def home():
    return render_template('home.html')


app.route('/register_user')
def register_user():
    controller = RegisterUserController()
    data = controller.read_all()
    return render_template('register_user.html', data=data)

# app.route('/register_user/form')
# def register_user_create():
#     register_id = request.args.get('id')
#     register_controller = RegisterUserController()
#     registers = register_controller.read_all()

#     if register_id:
#         controller = RegisterUserController()
#         data = controller.read_by_id(register_id)
#         return render_template('register_user_form.html', data=data, registers=registers) 
#     return render_template('register_user_form.html', registers=registers) 

# @app.route('/register_user/save')
# def register_user_save():
#     args_dict = request.args.to_dict(flat=False)
#     register_id = request.args.get('id')
#     name = request.args.get('name')
#     last_name = request.args.get('lastn_name')
#     user = request.args.get('user')
#     password = request.args.get('password')

#     controller = RegisterUserController()
#     if register_id: 
#         controller.update(register_id, name, last_name, user, password)
#     else:
#         controller.create(name, last_name, user, password)
#     return redirect('/register_user')


app.run()