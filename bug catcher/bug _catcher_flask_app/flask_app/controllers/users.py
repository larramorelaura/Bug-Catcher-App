from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.sticker import Sticker
from flask_app.models.order import Order
from flask_app.models.metamorphic_type import Type
from flask_app.models.insect import Insect
from flask_bcrypt import Bcrypt 


bcrypt = Bcrypt(app)

@app.route('/')
def root():
    if 'user_id' in session: 
        return redirect(f'/collection/{session["user_id"]}')
    return redirect('/register')

@app.route('/register')
def registration():
    return render_template('registration.html')

@app.route('/register/user', methods=['POST'])
def create():
    if not User.validator(request.form):
        return redirect('/register')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data= {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':pw_hash
    }
    id=User.save(data)
    return redirect(f'/collection/{id}')

@app.route('/edit/<int:id>')
def edit_profile(id):
    data={
        'id':id
    }
    user=User.get_one_by_id(data)
    return render_template('edit_profile.html', user=user)

@app.route('/collection/<int:id>')
def dashboard(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id
    }
    user=User.get_one_by_id(data)
    stickers=Sticker.get_collection(data)
    return render_template('collection.html', user=user, stickers=stickers)

@app.route('/logout', methods=['POST'])
def logout():
    del session['user_id']
    return redirect ('/')

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", 'log')
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", 'log')
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    print(session['user_id'])
    data={'id':session["user_id"]}
    logged_in_user=User.get_one_by_id(data)
    print(logged_in_user)
    # never render on a post!!!
    return redirect(f"/collection/{session['user_id']}")