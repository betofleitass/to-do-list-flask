from webbrowser import get
from flask import (Blueprint, flash, redirect, render_template,
                   url_for)
from flask_login import login_user, current_user
from app.forms import CreateToDoForm
from app.models import db, User, UserModel, get_user, ToDo

todo = Blueprint('todo', __name__, url_prefix='/todo')


@todo.route('/create', methods=['POST'])
def create_todo():

    create_todo_form = CreateToDoForm()

    if create_todo_form.validate_on_submit():
        user = current_user.id
        print(user)
        user_db = get_user(user)
        print(user_db)
        description = create_todo_form.description.data

        new_todo = ToDo(description=description, id_user=user_db.id)

        db.session.add(new_todo)
        db.session.commit()

        flash('To Do created successfully!', 'success')

        return redirect(url_for('index'))
