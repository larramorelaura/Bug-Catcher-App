from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def getting_survey():
    print(request.form)
    data={
        'name':request.form['name'],
        'location':request.form['location'],
        'language':request.form['language'],
        'comment':request.form['comments']
    } 
    
    if not User.validate_user(request.form):
        return redirect('/')
    id=User.save(data)
    # session['name']=request.form['name']
    # session['location']=request.form['location']
    # session['language']=request.form['language']
    # session['comments']=request.form['comments']
    # session['current']=request.form['options']
    # session['helps']=request.form.getlist('helps')
    # print(session['helps'])
    return redirect(f'/result/{id}')

@app.route('/result/<int:id>')
def submitted(id):
    data={
        'id':id
    }
    entry=User.get_user(data)
    return render_template('submit.html', entry=entry)