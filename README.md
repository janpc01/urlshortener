## Description
URL shortener API using Django REST Framework. You send a long URL and get a short code back. Hitting the short code redirects to the original.

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Testing
**Run unit tests**
```bash
pytest
```

## Usage
1. **Shorten a URL**
   ```bash
   curl -X POST http://127.0.0.1:8000/api/shorten/ \
        -H "Content-Type: application/json" \
        -d '{"original_url": "https://example.com/very/long/url"}'
   ```

2. **Redirect using short code**  
   Open in browser:
   ```
   http://127.0.0.1:8000/shrt/<short_code>/
   ```