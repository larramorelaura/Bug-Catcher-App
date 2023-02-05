from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
DATABASE = 'books_schema'

class Book:
    def __init__(self, data):
        self.id= data['id']
        self.title=data['title']
        self.pages=data['num_of_pages']
        self.favorite_authors =[]
        self.created_at= data['created_at']
        self.updated_at =data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(DATABASE).query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def save(cls, data):
        query ="INSERT INTO books (title, num_of_pages, created_at, updated_at)  VALUES (%(title)s, %(pages)s, NOW() , NOW() );"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_books_with_favorite_authors(cls, data):
        query= """SELECT * FROM books 
                LEFT JOIN favorites 
                ON favorites.book_id = books.id 
                LEFT JOIN authors 
                ON favorites.author_id = authors.id
                WHERE books.id=%(id)s"""
        result= connectToMySQL(DATABASE).query_db(query, data)
        if result:
            print(result)
            book=cls(result[0])
            for row_in_db in result:
                author_data={
                    'id':row_in_db['authors.id'],
                    'name':row_in_db['name'],
                    'created_at':row_in_db['authors.created_at'],
                    'updated_at':row_in_db['authors.updated_at']
                }
                book.favorite_authors.append(author.Author(author_data))
            return book
    
    @classmethod
    def book_favorite(cls,data):
        query= "INSERT INTO favorites (book_id, author_id) VALUES (%(bookid)s, %(authorid)s);"
        result= connectToMySQL(DATABASE).query_db(query, data)
        return result