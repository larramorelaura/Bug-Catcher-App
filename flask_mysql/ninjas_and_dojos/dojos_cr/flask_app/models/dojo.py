from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = 'dojos_and_ninjas'

class Dojo:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.created_at= data['created_at']
        self.updated_at =data['updated_at']

    
    
    @classmethod
    def save(cls, data):
        query ="INSERT INTO dojos (name, created_at, updated_at)  VALUES (%(name)s, NOW() , NOW() );"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_dojo_name(cls, data):
        query = "SELECT name FROM dojos WHERE id=%(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result