from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

# full crud routing
# home page for reading all users
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def read_all():
    users=User.get_all()
    print(users)
    return render_template('read(ALL).html', users=users)  # Return the string 'Hello World!' as a response

#form for creating a user
@app.route('/create')
def load_create():
    return render_template('create.html')


# post route for user
@app.route('/create_user', methods=['POST'])
def create_user():
    print(request.form)
    data ={
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    id = User.save(data)
    return redirect(f'/read_one/{id}')


# shows one user when clicked on show, created, or edited
@app.route('/read_one/<id>')
def read_one(id):
    print(id)
    data={
        'id': id
    }
    profile =User.show(data)
    print(profile)
    return render_template('read(ONE).html', profile=profile)


# creates the edit form based on the id retrieved
@app.route('/edit/<int:id>')
def edit(id):
    data={
        'id': id
    }
    info=User.edit_form(data)
    return render_template('edit.html', id=id, info=info)


# posts the edit from the form
@app.route('/edit_user/<int:id>', methods=['POST'])
def update(id):
    print(request.form)
    data ={
        'id': id,
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.update(data)
    return redirect(f'/read_one/{id}')

# route to delete a user
@app.route('/users/<id>/destroy')
def destroy_record(id):
    print(id)
    data ={
        'id':id
    }
    User.delete_user(data)
    return redirect('/')