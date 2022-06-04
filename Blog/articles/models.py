from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length = 100)
    img = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.title
    def snippet(self):
        return self.description[:50] + "..."
