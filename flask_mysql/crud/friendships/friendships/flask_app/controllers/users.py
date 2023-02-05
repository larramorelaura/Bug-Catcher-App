from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.friendship import Friendship

@app.route('/user/create', methods=['POST'])
def create_user():
    print(request.form)
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name']
    }
    User.save(data)
    return redirect('/friendships')