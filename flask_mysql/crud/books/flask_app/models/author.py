from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book
DATABASE = 'books_schema'

class Author:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.favorite_books=[]
        self.created_at= data['created_at']
        self.updated_at =data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            authors = []
            for author in results:
                authors.append(cls(author))
            return authors

    @classmethod
    def save(cls, data):
        query ="INSERT INTO authors (name, created_at, updated_at)  VALUES (%(name)s, NOW() , NOW() );"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
    
    @classmethod
    def get_authors_with_favorite_books(cls, data):
        query= """SELECT * FROM authors 
                LEFT JOIN favorites 
                ON favorites.author_id = authors.id 
                LEFT JOIN books 
                ON favorites.book_id = books.id 
                WHERE authors.id=%(id)s"""
        result= connectToMySQL(DATABASE).query_db(query, data)
        if result:
            print(result)
            author=cls(result[0])
            for row_in_db in result:
                book_data={
                    'id':row_in_db['books.id'],
                    'title':row_in_db['title'],
                    'num_of_pages':row_in_db['num_of_pages'],
                    'created_at':row_in_db['books.created_at'],
                    'updated_at':row_in_db['books.updated_at']
                }
                author.favorite_books.append(book.Book(book_data))
            return author

    @classmethod
    def save_favorite(cls,data):
        query= "INSERT INTO favorites (book_id, author_id) VALUES (%(bookid)s, %(authorid)s);"
        result= connectToMySQL(DATABASE).query_db(query, data)
        return result

