from flask import Flask, render_template, redirect, request, session  # Import Flask to allow us to create our app
from users import User
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    users=User.get_all()
    print(users)
    return render_template('read(ALL).html', users=users)  # Return the string 'Hello World!' as a response

@app.route('/create_user', methods=['POST'])
def create_user():
    print(request.form)
    data ={
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/read_one')

@app.route('/create')
def load_create():
    return render_template('create.html')

@app.route('/read_one/<id>')
def read_one(id):
    print(id)
    data={
        'id': id
    }
    profile =User.show(data)
    print(profile)
    return render_template('read(ONE).html', profile=profile)

@app.route('/edit/<int:id>')
def edit(id):
    data={
        'id': id
    }
    info=User.edit_form(data)
    return render_template('edit.html', id=id, info=info)

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

@app.route('/users/<id>/destroy')
def destroy_record(id):
    print(id)
    data ={
        'id':id
    }
    User.delete_user(data)
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.