from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
DATABASE = 'dojo_survey_schema'

class User:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.location=data['location']
        self.language=data['language']
        self.comment=data['comment']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def save(cls, data):
        query=""" 
                INSERT INTO dojos (name, location, language, comment, created_at, updated_at)
                VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());
                """
        result= connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def get_user(cls,data):
        query= "SELECT * FROM dojos WHERE id=%(id)s"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result:
            entry=cls(result[0])
        return entry

    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if user['location']== '-1':
            flash('Select a location')
            is_valid = False
        if user['language']== '-1':
            flash('Select a language')
            is_valid = False
        if len(user['comments']) < 3:
            flash("Comments must be at least 3 characters.")
            is_valid = False
        return is_valid