# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__(self, data):
        self.id= data['id']
        self.fname =data['first_name']
        self.lname= data['last_name']
        self.email= data['email']
        self.created_at= data['created_at']
        self.updated_at =data['updated_at']
    # ... other class methods
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_scheme').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    # class method to save our friend to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_scheme').query_db( query, data )

    @classmethod
    def show(cls, data):
        query="SELECT * FROM users WHERE id= %(id)s;"
        result = connectToMySQL('users_scheme').query_db( query, data)
        profile= cls(result[0])
        return profile

    @classmethod
    def delete_user(cls, data):
        query= "DELETE FROM users WHERE id= %(id)s;"
        return connectToMySQL('users_scheme').query_db( query, data )

    @classmethod
    def edit_form(cls, data):
        query= "SELECT * FROM users WHERE id= %(id)s;"
        result= connectToMySQL('users_scheme').query_db( query, data)
        info =cls(result[0])
        return info

    @classmethod
    def update(cls, data):
        query="UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at= NOW() WHERE id=%(id)s"
        return connectToMySQL('users_scheme').query_db( query, data )