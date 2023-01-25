from rest_framework import serializers

from .models import Dorama

class DoramaSerializer(serializers.ModelSerializer):

    stars = serializers.SerializerMethodField()

    def get_stars(self, obj: Dorama):
        dorama_reviews = obj.reviews.values()
        stars = 0

        for review in dorama_reviews:

            list_of_stars = list(review.values())
            stars += (list_of_stars[1])

        if len(dorama_reviews) == 0:
            return 'Esse dorama ainda não possui avaliações'
        
        dorama_stars = stars/len(dorama_reviews)
        return round(dorama_stars,2)


    class Meta:
        model = Dorama

        fields = '__all__'