from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    psoter_image = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return self.title

    def average_rating(self):
        reviews = self.ratings.all()
        if reviews.count()== 0:
            return 0
        total = sum(review.rating for review in reviews)
        return round(total / reviews.count(), 1)

class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} ({self.rating})"
    
