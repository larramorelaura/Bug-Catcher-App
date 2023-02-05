from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app import app
from flask import flash
DATABASE = 'friendships_schema'

class Friendship:
    def __init__(self, data):
        self.id= data['id']
        self.user_id=data['user_id']
        self.friend_id=data['friend_id']
        self.created_at= data['created_at']
        self.updated_at =data['updated_at']

    @classmethod
    def save_friendship(cls, data):
        query = """
            INSERT INTO friendships 
            ( user_id, friend_id, created_at, updated_at ) 
            VALUES ( %(user_id)s , %(friend_id)s , NOW() , NOW() );
            """
        # data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL(DATABASE).query_db( query, data )
        return result

    @classmethod
    def get_friends_by_id(cls,data):
        friends=[]
        query="""
            SELECT users.id 
            FROM friendships
            LEFT JOIN users
            ON friendships.friend_id= users.id
            WHERE user_id=%(user_id)s;
        """
        results=connectToMySQL(DATABASE).query_db(query,data)
        friends=results
        # print(friends)
        return friends

    @classmethod
    def get_friendships(cls):
        query="""
            SELECT * FROM friendships 
            LEFT JOIN users u
            ON friendships.friend_id = u.id
            LEFT JOIN users f
            ON friendships.user_id = f.id
            ORDER BY u.first_name;
        """
        results=connectToMySQL(DATABASE).query_db(query)
        # print(results)
        if results:
            friendships=[]
            for row in results:
                friendship=cls(row)
                user_data ={
                    'id':row['u.id'],
                    'first_name':row['first_name'],
                    'last_name':row['last_name'],
                    'created_at':row['created_at'],
                    'updated_at':row['updated_at']
                }
                friend_data = {
                    'id':row['f.id'],
                    'first_name':row['f.first_name'],
                    'last_name':row['f.last_name'],
                    'created_at':row['f.created_at'],
                    'updated_at':row['f.updated_at']
                }
                first_friend=user.User(user_data)
                second_friend=user.User(friend_data)
                friendship.first_friend=first_friend
                friendship.second_friend=second_friend
                # print(friendship)
                friendships.append(friendship)
        return friendships

    @classmethod
    def get_unfriended_users(data):
        query = """
            SELECT * FROM users 
            WHERE users.first_name NOT IN
            (SELECT users.first_name 
            FROM friendships
            JOIN users
            ON friendships.friend_id= users.id
            WHERE user_id=%(id)s);
            """
        results=connectToMySQL(DATABASE).query_db(query,data)
        return results

    @staticmethod
    def friend_validator(friendship):
        print(friendship)
        is_valid=True
        if int(friendship['friend_id']) == int(friendship['user']):
            flash("You can't friend yourself!", 'friend')
            is_valid=False
        data={
            'user_id':friendship['user']
        }
        friends=Friendship.get_friends_by_id(data)
        print(friends)
        print(friendship['friend_id'])
        for friend in friends:
            if  friend['id']==int(friendship['friend_id']):
                flash("Friendship already exits", 'friend')
                is_valid=False
        return is_valid