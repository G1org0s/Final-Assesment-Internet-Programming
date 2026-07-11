from django.db import models


# This table keeps the reviews that customers write.
class Review(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    fish = models.CharField(max_length=80)
    message = models.TextField(max_length=200)
    recommend = models.CharField(max_length=3)
    stars = models.IntegerField(default=0)

    # This makes the admin page show the review location.
    def __str__(self):
        return self.location
