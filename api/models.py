from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=30)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ['-created_datetime']
    
    def __str__(self):
        return self.title
    
    