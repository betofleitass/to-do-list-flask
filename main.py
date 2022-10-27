from typing import List


from flask import (flash, make_response,
                   redirect, render_template, request,
                   session, url_for, Response)
from flask_login import current_user


from app import create_app
from app.forms import CreateToDoForm, DeleteToDoForm, LoginForm
from app.models import db, get_user_todo_list, get_user


app = create_app()
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/", methods=['GET'])
def index() -> str:

    login_form = LoginForm()

    context = {
        'login_form': login_form,

    }

    # If the user is logged in
    if not current_user.is_anonymous:
        username = current_user.id
        create_todo_form = CreateToDoForm()
        delete_todo_form = DeleteToDoForm()
        # Get the user todo list
        user = current_user.id
        user_db = get_user(user)
        todo_list = get_user_todo_list(id_user=user_db.id)
        context = {
            "username": username,
            "create_todo_form": create_todo_form,
            "delete_todo_form": delete_todo_form,
            "todo_list": todo_list
        }

        return render_template("index.html", **context)

    return render_template("index.html", **context)


if __name__ == "__main__":
    app.run(port=5000,
            debug=True)
