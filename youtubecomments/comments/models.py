from django.db import models

# Create your models here.
class Comment(models.Model):
    video_id = models.CharField(max_length=50)
    comment_content = models.CharField(max_length=500)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    
