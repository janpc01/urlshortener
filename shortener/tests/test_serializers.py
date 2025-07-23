import pytest
from shortener.serializers import ShortURLSerializer
from shortener.models import ShortURL

@pytest.mark.django_db
def test_serializer_generates_short_code():
    serializer = ShortURLSerializer(data={"original_url": "https://example.com"})
    assert serializer.is_valid()
    instance = serializer.save()
    assert instance.short_code is not None
    assert isinstance(instance.short_code, str)
    assert len(instance.short_code) == 6

@pytest.mark.django_db
def test_serializer_rejects_invalid_url():
    serializer = ShortURLSerializer(data={"original_url": "not-a-url"})
    assert not serializer.is_valid()
    assert "original_url" in serializer.errors