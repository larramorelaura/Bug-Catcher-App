from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.friendship import Friendship

@app.route('/')
def home():
    return redirect ('/friendships')

@app.route('/friendships')
def friendship_page():
    users=User.get_all()
    friendships=Friendship.get_friendships()
    return render_template('friendships.html', users=users, friendships=friendships)

# @app.route('/friendship/first_friend', methods=['POST'])
# def get_not_friends():
#     data={
#         request.form['user']
#     }
    # unfriended_users=Friendship.get_unfriended_users(data)
    


@app.route('/friendship/create', methods=['POST'])
def create_friendship():
    print(request.form)
    if not Friendship.friend_validator(request.form):
        return redirect('/')
    data={
        'user_id':request.form['user'],
        'friend_id': request.form['friend_id']
    }
    Friendship.save_friendship(data)
    return redirect('/friendships')

