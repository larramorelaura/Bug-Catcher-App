from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import friendship
DATABASE = 'friendships_schema'

class User:
    def __init__(self, data):
        self.id= data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.created_at= data['created_at']
        self.updated_at =data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO users 
            ( first_name , last_name , created_at, updated_at ) 
            VALUES ( %(first_name)s , %(last_name)s , NOW() , NOW() );
            """
        # data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL(DATABASE).query_db( query, data )
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            users = []
            for user in results:
                users.append(cls(user))
            return users

    @classmethod
    def get_all_with_friends(cls):
        query= """
        	SELECT * FROM users
            LEFT JOIN friendships
            ON friendships.user_id=users.id
            LEFT JOIN users f
            ON friendships.friend_id=f.id; 
        	"""  
        #edit using table names#

        result= connectToMySQL(DATABASE).query_db(query)

        #if there is results get the resutls in a cls and then rename keys that overlap#

        if result:
            print(result)
            users=[]
            for row in result:
                first_friend=cls(row)
                friend_data={
                    'id':row['f.id'],
                    'first_name':row['f.first_name'],
                    'last_name':row['f.last_name'],
                    'created_at':row['f.created_at'],
                    'updated_at':row['f.updated_at']
                }
                friend=cls(friend_data)
                first_friend.friend=friend
                users.append(first_friend)
                print(users)
        return users