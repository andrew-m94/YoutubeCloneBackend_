from django.db import models

# Create your models here.
class Reply(models.Model):
    comment_id = models.IntegerField()
    reply_content = models.CharField(max_length=500)
    likes = models.IntegerField()
    dislikes = models.IntegerField()