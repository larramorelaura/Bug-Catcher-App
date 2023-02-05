from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'keep it secret, keep it safe'

count=0
@app.route('/')
def home():
    global count
    count+=1
    if 'count' not in session:
        session['count']=1
    else:
        session['count']+=1
    print(session['count'])
    return render_template('index.html', count=session['count'], total=count)

@app.route('/count')
def count_rt():
    global count
    count+=2
    if 'count' in session:
        session['count']+=2
    return render_template('index.html', count=session['count'], total=count)

@app.route('/add', methods=['POST'])
def add_count():
    global count
    print('Number for count')
    print(request.form)
    session['counter_item']=request.form['counter']
    if 'counter_item' in session:
        print('key exists!')
        session['count']+=int(session['counter_item'])
        count+=int(session['counter_item'])
    else:
        print("key 'counter' does NOT exist")
    return redirect('/')

@app.route('/destroy_session')
def clear_session():
    global count
    count+=session.pop('count')
    return redirect ('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.