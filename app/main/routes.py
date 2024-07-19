from flask import render_template, request, redirect, url_for, flash
from app.main import bp as main
from app.models import Item
from app import db

@main.route('/')
def index():
    items = Item.query.all()

    title = "Welcome to Your Flask App"
    description = "This is a sample Flask application using Jinja2 templates."
    return render_template('main/index.html', title=title, description=description, items=items)

@main.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_item = Item(name=name, description=description)
        db.session.add(new_item)
        db.session.commit()
        flash('Item added successfully!')
        return redirect(url_for('main.index'))
    return render_template('main/add_item.html')

@main.route('/update/<int:id>', methods=['GET', 'POST'])
def update_item(id):
    item = Item.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.description = request.form['description']
        db.session.commit()
        flash('Item updated successfully!')
        return redirect(url_for('main.index'))
    return render_template('main/update_item.html', item=item)

@main.route('/delete/<int:id>', methods=['POST'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted successfully!')
    return redirect(url_for('main.index'))