from shortener.models import ShortURL

def test_model_str():
    obj = ShortURL(original_url="https://example.com", short_code="abc123")
    assert str(obj) == "abc123 -> https://example.com"