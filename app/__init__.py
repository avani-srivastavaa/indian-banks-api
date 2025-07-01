from flask import Flask
from flask_graphql import GraphQLView
from .extensions import db
from .schema import schema

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    db.init_app(app)

    # ✅ Register the /gql route inside create_app
    app.add_url_rule(
        '/gql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )

    @app.route('/')
    def home():
        return '✅ API is running. Visit /gql for GraphQL interface.'

    return app
