from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/dojos')
def home():
    dojos=Dojo.get_all()
    print(dojos)
    return render_template('dojos.html', dojos=dojos)

@app.route('/dojos/new', methods=["POST"])
def new_dojo():
    print(request.form)
    data ={
        'name': request.form['dojo_name']
    }
    id = Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<id>')
def show_dojos(id):
    print(id)
    data={
        'id':id
    }
    ninjas=Ninja.show(data)
    dojo=Dojo.get_dojo_name(data)
    print(dojo)
    for entry in dojo:
        dojo_name= entry['name']
    return render_template('ninjas.html', ninjas=ninjas, dojo_name=dojo_name)
