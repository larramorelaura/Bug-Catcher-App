from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def default_board():
    return render_template('blocks.html', x=4, y=4)

@app.route('/<int:x>')
def four_by_four(x):
    return render_template('blocks.html', x=(x//2), y=4)

@app.route('/<int:x>/<int:y>')
def custom(x, y):
    return render_template('blocks.html', x=(x//2), y=(y//2))

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def all_custom(x, y, color1, color2):
    return render_template('blocks.html', x=(x//2), y=(y//2), color1=color1, color2=color2)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="0.0.0.0")    # Run the app in debug mode.

