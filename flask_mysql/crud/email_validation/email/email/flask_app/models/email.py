from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATABASE = 'emails_schema'

class Email:
    def __init__(self, data):
        self.id=data['id']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def save(cls, data):
        query="""
            INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());
            """
        result= connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_all(cls):
        query="""
            SELECT * FROM emails
        """
        results=connectToMySQL(DATABASE).query_db(query)
        if results:
            users=[]
            for item in results:
                users.append(cls(item))
        return users

    @classmethod
    def get_one(cls,data):
        query= """
            SELECT * FROM emails WHERE id=%(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result:
            one = cls(result[0])
        return one

    @staticmethod
    def validator(email):
        is_valid= True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,email)
        if len(results) >=1:
            flash("Email already taken.")
            is_valid=False
        elif not EMAIL_REGEX.match(email): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid