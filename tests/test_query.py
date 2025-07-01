import json
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_branches_query(client):
    query = '''
    {
        branches {
            edges {
                node {
                    ifsc
                    branch
                    bank {
                        name
                    }
                }
            }
        }
    }
    '''
    response = client.post('/gql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'branches' in response.json['data']
