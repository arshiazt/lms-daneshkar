import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_test_view_get(client):
    url = reverse('test')
    response = client.get(url)
    assert response.status_code == 200
    assert 'text/html' in response['Content-Type']

@pytest.mark.django_db
def test_test_view_get_renders_template(client):
    url = reverse('test')
    response = client.get(url)
    assert 'test.html' in {t.name for t in response.templates}

@pytest.mark.django_db
def test_test_view_post(client):
    url = reverse('test')
    data = {
        'name':'arshia',
        'message':'hello'
    }
    response = client.post(url,data)
    assert response.status_code == 200
    assert 'arshia hello' 