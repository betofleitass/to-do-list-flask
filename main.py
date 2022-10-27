from flask import (flash, make_response,
                   redirect, render_template, request,
                   session, url_for, Response)

from app import create_app
from app.forms import LoginForm
from app.models import db


app = create_app()
db.init_app(app)

with app.app_context():
    db.create_all()


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
