from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play')
def play():
    return render_template('plays.html', times=3)

@app.route('/play/<int:times>')
def repeat_play(times):
    return render_template('plays.html', times=times)

@app.route('/play/<int:times>/<color>')
def pretty(times, color):
    return render_template('plays.html', times=times, color=color)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.