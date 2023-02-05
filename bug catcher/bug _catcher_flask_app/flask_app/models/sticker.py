from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models.order import Order
DATABASE = 'mydb'

class Sticker:
    def __init__(self, data):
        self.id=data['id']
        self.description=data['description']
        self.filename= data ['filename']
        self.created_at= data['created_at']
        self.updated_at =data['updated_at']

    @classmethod
    def get_collection(cls,data):
        query="""
            SELECT * FROM stickers 
            LEFT JOIN orders_stickers
            ON orders_stickers.sticker_id=stickers.id
            LEFT JOIN orders 
            ON orders.id =orders_stickers.order_id
            LEFT JOIN collections
            ON collections.sticker_id= stickers.id
            LEFT JOIN users
            ON users.id =collections.user_id
            WHERE collections.user_id=%(id)s;
        """
        results=connectToMySQL(DATABASE).query_db(query, data)
        stickers=[]
        if results:
            for row in results:
                sticker=cls(row)
                order_data={
                    **row,
                    'id': row['order_id'],
                    'created_at': row['orders.created_at'],
                    'updated_at': row['orders.updated_at']
                }
                order = Order(order_data)
                sticker.order=order
                stickers.append(sticker)
        return stickers

    @classmethod
    def get_stickers_by_species(cls,data):
        query= """
            SELECT * FROM stickers 
            LEFT JOIN species
            ON stickers.specie_id=species.id
            WHERE species.id=%(id)s;
        """
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            stickers=[]
            for row in result:
                sticker=cls(row)
                stickers.append(sticker)

        return stickers

    @classmethod
    def add_stickers(cls, data):
        query= """
            INSERT INTO collections (user_id, sticker_id, created_at, updated_at) VALUES(%(user_id)s, %(id)s, NOW(), NOW());
        """
        result=connectToMySQL(DATABASE).query_db(query, data)
        return result