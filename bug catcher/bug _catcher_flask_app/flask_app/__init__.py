from flask import Flask, render_template, redirect, request, session
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'config/UPLOAD_FOLDER'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = "shhhhhh"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER