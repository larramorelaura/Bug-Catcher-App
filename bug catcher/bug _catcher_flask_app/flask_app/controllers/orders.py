from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.sticker import Sticker
from flask_app.models.order import Order
from flask_app.models.metamorphic_type import Type
from flask_app.models.insect import Insect

@app.route('/order/<int:id>')
def show_order_info(id):
    data={
        'id':id
    }
    order= Order.get_one_by_id(data)
    user_id=session['user_id']
    fact=Insect.get_random_fact()
    return render_template ('species_info.html', order=order, user_id=user_id, fact=fact)