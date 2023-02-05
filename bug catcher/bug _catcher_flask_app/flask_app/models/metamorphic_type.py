from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app

DATABASE = 'mydb'

class Type:
    def __init__(self, data):
        self.id=data['id']
        self.types=data['types']
        self.stage_one= data ['stage_one']
        self.stage_two=data['stage_two']
        self.stage_three=data['stage_three']
        self.stage_four=data['stage_four']
        self.created_at= data['created_at']
        self.updated_at =data['updated_at']