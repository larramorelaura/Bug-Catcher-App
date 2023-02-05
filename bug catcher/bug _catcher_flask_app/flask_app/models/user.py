from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import insect
from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
import re

DATABASE = 'mydb'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id= data['id']
        self.first_name =data['first_name']
        self.last_name= data['last_name']
        self.email= data['email']
        self.password=data['password']
        self.created_at= data['created_at']
        self.updated_at =data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , password, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL(DATABASE).query_db( query, data )
        return result

    @classmethod
    def get_one_by_id(cls, data):
        query="SELECT * FROM users WHERE id= %(id)s;"
        result = connectToMySQL(DATABASE).query_db( query, data)
        user= cls(result[0])
        return user

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validator(user):
        is_valid= True
        if len(user['first_name']) < 2:
            flash("Please enter a First Name.", 'reg')
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Please enter a Last Name.", 'reg')
            is_valid = False
        if len(user['email']) < 1:
            flash("Please enter an email.", 'reg')
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'reg')
            is_valid = False
        else:
            data={
                'email':user['email']
            }
            potential_user=User.get_by_email(data)
            if potential_user:
                flash('Email already registered.', 'reg')
                is_valid =False
        if len(user['password'])< 8:
            flash("Please create password. Password must be 8 characters", 'reg')
            is_valid=False
        if user['password'] != user['confirm_password']:
            flash("Passwords do not match.", 'reg')
            is_valid = False
        return is_valid
        