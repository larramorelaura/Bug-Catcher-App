from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import user
DATABASE = 'recipe_schema' 

class Recipe:
    def __init__(self, data):
        self.id= data['id']
        self.name =data['name']
        self.description= data['description']
        self.instructions= data['instructions']
        self.time=data['time']
        self.date=data['date']
        self.created_at= data['created_at']
        self.updated_at =data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, time, date, created_at, updated_at, user_id ) VALUES (%(name)s , %(description)s , %(instructions)s, %(time)s, %(date)s, NOW() , NOW(), %(user_id)s);"
        # data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL(DATABASE).query_db( query, data )
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            recipes = []
            for recipe in results:
                recipes.append(cls(recipe))
            return recipes

    @classmethod
    def get_one(cls, data):
        query="SELECT * FROM recipes WHERE id= %(id)s;"
        result = connectToMySQL(DATABASE).query_db( query, data)
        profile= cls(result[0])
        return profile

    @classmethod
    def get_recipes_with_user(cls):
        query= """
            SELECT * FROM recipes
            JOIN users
            ON users.id = recipes.user_id;
            """
        results=connectToMySQL(DATABASE).query_db(query)
        recipes=[] 
        if results:
            for row in results:
                print(row['first_name'])
                recipe= cls(row)
                user_data ={
                    **row,
                    'id': row['users.id'],
                    'created_at':row['users.created_at'],
                    'updated_at':row['users.updated_at']
                }
                poster=user.User(user_data)
                recipe.poster=poster
                recipes.append(recipe)
        return recipes

    @classmethod
    def update(cls, data):
        query="UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, time=%(time)s, date=%(date)s, updated_at= NOW() WHERE recipes.id=%(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def get_recipe_with_user(cls,data):
        query= """
            SELECT * FROM recipes
            JOIN users
            ON users.id = recipes.user_id
            WHERE recipes.id = %(id)s;
            """
        results=connectToMySQL(DATABASE).query_db(query,data)

        if results:
            recipe= cls(results[0])
            for row in results:
                user_data ={
                    **row,
                    'id': row['users.id'],
                    'created_at':row['users.created_at'],
                    'updated_at':row['users.updated_at']
                }
                poster=user.User(user_data)
                recipe.poster=poster
                print(recipe)
            return recipe

    @classmethod
    def delete_recipe(cls, data):
        query= "DELETE FROM recipes WHERE id= %(id)s;"
        return connectToMySQL(DATABASE).query_db( query, data )

    @staticmethod
    def validator_recipe(recipe):
        is_valid= True
        if len(recipe['name']) < 3:
            flash("Recipe name must be 3 characters.", 'recipe')
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description must be 3 characters.", 'recipe')
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("Instructions must be 3 characters.", 'recipe')
            is_valid = False
    # radio button validate
        if 'time' not in recipe:
            flash("Select if it is under 30 minutes.", 'recipe')
            is_valid = False
        if len(recipe['date']) < 3:
            flash("Please choose a date.", 'recipe')
            is_valid = False
        return is_valid
