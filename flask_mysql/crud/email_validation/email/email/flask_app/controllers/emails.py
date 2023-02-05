from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.email import Email

@app.route('/')
def home():
    return render_template('input_email.html')

@app.route('/email/create', methods=['POST'])
def create():
    if not Email.validator(request.form):
        return redirect('/')
    print(request.form)
    data={
        'email':request.form['email']
    }
    id=Email.save(data)
    return redirect (f'/success/{id}')

@app.route('/success/<int:id>')
def success(id):
    data={
        'id':id
    }
    email=Email.get_one(data)
    users=Email.get_all()
    return render_template('success.html', email=email, users=users)