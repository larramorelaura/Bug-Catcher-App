from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninja_form():
    dojos=Dojo.get_all()
    return render_template('create_ninja.html', dojos=dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    print(request.form)
    data ={
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'age': request.form['age'],
        'dojo_id':request.form['dojo']#check into this syntax
    }
    id= request.form['dojo']
    Ninja.save(data)
    return redirect(f'/dojos/{id}')

