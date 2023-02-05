from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def getting_survey():
    print(request.form)
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comments']=request.form['comments']
    session['current']=request.form['options']
    session['helps']=request.form.getlist('helps')
    print(session['helps'])
    return redirect('/result')

@app.route('/result')
def submitted():
    return render_template('submit.html', name=session['name'], location=session['location'], language=session['language'], comments=session['comments'], help=session['helps'], student=session['current'])


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.