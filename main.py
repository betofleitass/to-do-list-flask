from flask import (flash, make_response,
                   redirect, render_template, request,
                   session, url_for, Response)

from flask_sqlalchemy import SQLAlchemy
from app import create_app
from app.forms import LoginForm


app = create_app()
# Database configuration
db = SQLAlchemy()
db.init_app(app)


@app.route("/", methods=['GET'])
def index() -> str:
    login_form = LoginForm()
    context = {
        "login_form": login_form,
    }

    return render_template("index.html", **context)


if __name__ == "__main__":
    app.run(port=5000,
            debug=True)
