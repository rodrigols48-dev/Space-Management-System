from flask import Blueprint, render_template, url_for, flash, redirect, request
from app import db
from app.models import Space
from app.forms import SpaceForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    spaces = Space.query.all()
    return render_template('index.html', spaces=spaces)

@bp.route('/add', methods=['GET', 'POST'])
def add_space():
    form = SpaceForm()
    if form.validate_on_submit():
        space = Space(name=form.name.data, description=form.description.data)
        db.session.add(space)
        db.session.commit()
        flash('Space added successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('add_space.html', form=form)

@bp.route('/edit/<int:space_id>', methods=['GET', 'POST'])
def edit_space(space_id):
    space = Space.query.get_or_404(space_id)
    form = SpaceForm()
    if form.validate_on_submit():
        space.name = form.name.data
        space.description = form.description.data
        db.session.commit()
        flash('Space updated successfully!', 'success')
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        form.name.data = space.name
        form.description.data = space.description
    return render_template('edit_space.html', form=form)

@bp.route('/delete/<int:space_id>', methods=['POST'])
def delete_space(space_id):
    space = Space.query.get_or_404(space_id)
    db.session.delete(space)
    db.session.commit()
    flash('Space deleted successfully!', 'success')
    return redirect(url_for('main.index'))
