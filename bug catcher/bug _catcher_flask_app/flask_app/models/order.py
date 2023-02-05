from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import metamorphic_type
DATABASE = 'mydb'

class Order:
    def __init__(self, data):
        self.id=data['id']
        self.name_of_order=data['name_of_order']
        self.identifiers= data ['identifiers']
        self.food=data['food']
        self.created_at= data['created_at']
        self.updated_at =data['updated_at']

    @classmethod
    def get_one_by_id(cls, data):
        query= """
            SELECT * FROM orders
            LEFT JOIN metamorphic_types
            ON orders.metamorphic_type_id =metamorphic_types.id
            WHERE orders.id=%(id)s;
        """
        result=connectToMySQL(DATABASE).query_db(query, data)
        order=cls(result[0])
        for row in result:
            
            type_data ={
                **row,
                'id': row['metamorphic_types.id']
            }
            metamorphosis=metamorphic_type.Type(type_data)
            order.metamorphosis=metamorphosis
        return order