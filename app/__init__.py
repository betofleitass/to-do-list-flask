import os

from flask import Flask


# Application factory function
def create_app(test_config=None) -> Flask:
    """
    Creates the Flask instance and configure it

    Keyword arguments:
    test_config: str (optional) -> description

    Return:
    app: Flask -> Flask instance
    """

    app = Flask(__name__, instance_relative_config=True)
    # Set some default configuration
    app.config.from_mapping(
        SECRET_KEY='SUPER_SECRET_KEY',
        DATABASE=os.path.join(app.instance_path, 'database.sqlite'),
    )

    if test_config is None:
        # Loads the instance config
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Loads the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
