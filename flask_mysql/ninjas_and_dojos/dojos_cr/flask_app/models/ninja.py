from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = 'dojos_and_ninjas'

class Ninja:
    def __init__(self, data):
        self.id=data['id']
        self.fname=data['first_name']
        self.lname=data['last_name']
        self.age=data['age']
        self.dojo_id= data['dojo_id']
        self.created_at= data['created_at']
        self.updated_at =data['updated_at']

    @classmethod
    def save(cls, data):
        query ="INSERT INTO ninjas ( first_name , last_name , age , dojo_id, created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(age)s , %(dojo_id)s, NOW() , NOW() );"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def show(cls, data):
        query= "SELECT * FROM ninjas WHERE dojo_id=%(id)s"
        results = connectToMySQL(DATABASE).query_db( query, data)
        ninjas =[]
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas