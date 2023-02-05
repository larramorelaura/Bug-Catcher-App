from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import user, order, sticker, metamorphic_type
import random
DATABASE = 'mydb'

class Insect:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.created_at= data['created_at']
        self.updated_at =data['updated_at']

    @classmethod
    def get_species_id(cls, data):
        query="""
            SELECT species.id 
            FROM species
            WHERE species.name=%(name)s;
        """
        result= connectToMySQL(DATABASE).query_db(query,data)
        for row in result:
            return row['id']

    @classmethod
    def get_random_fact(cls):
        data={
            'num':random.randint(1,22)
        }
        query= """
            SELECT random_facts.fact FROM random_facts WHERE id=%(num)s;
        """
        result =connectToMySQL(DATABASE).query_db(query,data)
        for row in result:
            return row['fact']