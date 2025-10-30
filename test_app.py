import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Teste simples para verificar se a página inicial carrega corretamente"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Olá, mundo!" in response.data
