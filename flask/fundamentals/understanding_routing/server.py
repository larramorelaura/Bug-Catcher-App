from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_name(name):
    print(name)
    return 'Hi '+ name.capitalize()+"!"

@app.route('/repeat/<int:times>/<string:word>')
def repeat_word(times, word):
    print(times, word)
    word_display = ''
    for i in range(0,times):
        word_display += f"<p>{word}</p>"
    return word_display

@app.errorhandler(404)
def not_found(e):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

