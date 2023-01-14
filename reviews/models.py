from django.db import models

class Review(models.Model):

    stars = models.IntegerField()
    review = models.CharField(max_length=400)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name= 'reviews')
    dorama_id = models.ForeignKey('doramas.Dorama', on_delete=models.CASCADE, related_name= 'reviews')

    REQUIRED_FIELDS = ['stars']

