import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from shortener.models import ShortURL

@pytest.mark.django_db
def test_create_short_url():
    client = APIClient()
    response = client.post(reverse("shorten"), {"original_url": "https://example.com"}, format='json')
    assert response.status_code == 201
    assert "short_code" in response.data

@pytest.mark.django_db
def test_redirect_short_url():
    client = APIClient()
    url = ShortURL.objects.create(original_url="https://example.com", short_code="abc123")
    response = client.get(f"/shrt/{url.short_code}/")
    assert response.status_code == 302
    assert response.url == url.original_url

@pytest.mark.django_db
def test_invalid_url_submission():
    client = APIClient()
    response = client.post(reverse("shorten"), {"original_url": "not-a-url"}, format='json')
    assert response.status_code == 400
    assert "original_url" in response.data

@pytest.mark.django_db
def test_short_code_collision(monkeypatch):
    ShortURL.objects.create(original_url="https://first.com", short_code="abc123")
    codes = iter(["abc123", "def456"])
    monkeypatch.setattr("shortener.serializers.generate_code", lambda: next(codes))

    client = APIClient()
    response = client.post(reverse("shorten"), {"original_url": "https://second.com"}, format='json')
    assert response.status_code == 201
    assert response.data["short_code"] == "def456"

@pytest.mark.django_db
def test_redirect_404_for_unknown_code():
    client = APIClient()
    response = client.get("/shrt/doesnotexist/")
    assert response.status_code == 404