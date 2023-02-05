from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from flask_app.models.user import User
from flask_app.models.sticker import Sticker
from flask_app.models.order import Order
from flask_app.models.metamorphic_type import Type
from flask_app.models.insect import Insect
import os, io
from google.cloud import vision
from google.cloud import storage


app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.jpeg']
app.config['UPLOAD_PATH'] ='UPLOAD_FOLDER/'

def localize_objects(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(
        image=image).localized_object_annotations
    print(objects)
    print('Number of objects found: {}'.format(len(objects)))
    names=[]
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        names.append(object_.name)
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))
    print(names)
    return names[0]



def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


client = vision.ImageAnnotatorClient()


@app.route('/upload', methods=['GET','POST'])
def upload_photo():
    print(request.files)
    if request.method == "POST":
        photo = request.files['id_photo']
        # print('photo here')
        # print(photo)
        # photo_bytes=photo.read()
        # photo_data ={
        #     'photo':photo_bytes,
        #     'photo_name':f"{photo.filename}"
        # }
        species_id=2
        filename = secure_filename(photo.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
        photo.save(os.path.join(app.config['UPLOAD_PATH'], filename))

        name=localize_objects(os.path.join(app.config['UPLOAD_PATH'], filename))
        print(name)
        data={
            'name':name
        }
        species_id=Insect.get_species_id(data)
        # species_id=json request from google vision with order given an id
    return redirect(url_for('show_id', name = name, id=species_id))
    

@app.route('/species_id/<int:id>/<string:name>')
def show_id(id,name):
    data ={
        'id':id
    }
    sticker_choices=Sticker.get_stickers_by_species(data)
    data={
        'id':session['user_id']
    }
    name=name
    user=User.get_one_by_id(data)
    return render_template('species_id.html', sticker_choices=sticker_choices, user=user, name=name)

@app.route('/new/stickers/create', methods=['POST'])
def add_stickers():
    print(request.form)
    data= {
        'id':request.form['new_sticker'],
        'user_id':session['user_id']
    }
    Sticker.add_stickers(data)
    return redirect(f'/collection/{session["user_id"]}')


