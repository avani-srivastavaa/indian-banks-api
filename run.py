from flask import Flask
from flask_graphql import GraphQLView
from app import create_app
from app.schema import schema

app = create_app()

app.add_url_rule(
    '/gql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

if __name__ == '__main__':
    app.run(debug=True)
