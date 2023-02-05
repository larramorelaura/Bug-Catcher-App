from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.route('/authors')
def authors():
    authors=Author.get_all()
    print(authors)
    return render_template('authors.html', authors=authors)

@app.route('/authors/<int:id>')
def authors_favorites(id):
    data ={
        'id':id
    }
    author=Author.get_authors_with_favorite_books(data)
    books=Book.get_all()
    return render_template('author_show.html', author=author, books=books)

@app.route('/authors/create', methods=['POST'])
def add_author():
    print(request.form)
    data ={
        'name': request.form['author']
    }
    id = Author.save(data)
    return redirect('/authors')

@app.route('/authors/favorites/create/<int:author_id>', methods=['POST'])
def add_favorite(author_id):
    print(request.form)
    data ={
        'authorid': author_id,
        'bookid': request.form['book']
    }
    Author.save_favorite(data)
    return redirect(f'/authors/{author_id}')



