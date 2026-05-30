from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='movies/')
    duration = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return self.title
    
class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    timing = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.movie.title} - {self.timing}"
    
