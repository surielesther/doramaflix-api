from rest_framework import serializers
from .models import Dorama

class DoramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dorama

        fields = '__all__'
        # [
        #     'id',
        #     'stars',
        #     'review',
        #     'user_id',
        #     'dorama_id',
        # ]