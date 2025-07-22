from rest_framework import serializers
from .models import ShortURL
from .utils import generate_code

class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ['original_url', 'short_code']
        read_only_fields = ['short_code']

    def create(self, validated_data):
        code = generate_code()

        while ShortURL.objects.filter(short_code=code).exists():
            code = generate_code()
        
        validated_data['short_code'] = code
        return super().create(validated_data)