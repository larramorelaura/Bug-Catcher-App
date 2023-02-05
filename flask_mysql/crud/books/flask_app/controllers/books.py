from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/books/create', methods=['POST'])
def add_book():
    print(request.form)
    data ={
        'title': request.form['title'],
        'pages': request.form['pages']
    }
    Book.save(data)
    return redirect('/books')

@app.route('/books/favorites/create/<int:book_id>', methods=['POST'])
def book_favorite(book_id):
    print(request.form)
    data ={
        'authorid': request.form['author'],
        'bookid': book_id
    }
    Book.book_favorite(data)
    return redirect(f'/books/{book_id}')

@app.route('/books/<int:id>')
def books_favorites(id):
    data ={
        'id':id
    }
    book=Book.get_books_with_favorite_authors(data)
    authors=Author.get_all()
    return render_template('book_show.html', authors=authors, book=book)

@app.route('/books')
def books():
    books=Book.get_all()
    return render_template('books.html', books=books)