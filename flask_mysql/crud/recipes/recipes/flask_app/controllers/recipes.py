from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/dashboard/<int:id>')
def dashboard(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id
    }
    user=User.get_one_by_id(data)
    recipes=Recipe.get_recipes_with_user()
    print(recipes)
    return render_template('dashboard.html', recipes=recipes, user=user)

@app.route('/recipes/update/<int:id>', methods=['POST'])
def update_recipe(id):
    print(request.form)
    if not Recipe.validator_recipe(request.form):
        return redirect(f'/recipes/edit/{id}')
    data ={
        'id': id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'time': request.form['time'],
        'date': request.form['date']
    }
    Recipe.update(data)
    return redirect(f'/dashboard/{session["user_id"]}')

@app.route('/recipes/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':id
    }
    recipe=Recipe.get_one(data)
    data={
        'id':session['user_id']
    }
    user=User.get_one_by_id(data)
    return render_template('edit_recipe.html', recipe=recipe, user=user)

@app.route('/recipes/new')
def generate_form():
    if 'user_id' not in session:
        return redirect('/')
    data={
        'id':session['user_id']
    }
    user=User.get_one_by_id(data)
    return render_template('create_recipe.html', user=user)

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    if not Recipe.validator_recipe(request.form):
        return redirect('/recipes/new')
    data ={
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'time': request.form['time'],
        'date': request.form['date'],
        'user_id':session['user_id']
    }
    Recipe.save(data)
    return redirect(f'/dashboard/{session["user_id"]}')

@app.route('/recipes/<int:id>')
def show_one(id):
    data={
        'id':id
    }
    recipe=Recipe.get_recipe_with_user(data)
    data = {
        'id':session['user_id']
    }
    user=User.get_one_by_id(data)
    return render_template('one_recipe.html', recipe=recipe, user=user)

@app.route('/recipes/delete/<int:id>')
def remove(id):
    data={
        'id':id
    }
    Recipe.delete_recipe(data)
    
    return redirect(f'/dashboard/{session["user_id"]}')