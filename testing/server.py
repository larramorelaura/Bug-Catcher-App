from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "shhhhhh"
# Import Flask to allow us to create our app

import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('resources/bumblebee.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 