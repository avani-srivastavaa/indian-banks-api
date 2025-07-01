from flask import Flask
from .extensions import db  

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    db.init_app(app)

    @app.route('/')
    def home():
        return '✅ GraphQL API is running! Visit /gql to explore.'


    return app
