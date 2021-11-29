from django.db import models
from comments.models import Comment

# Create your models here.
class Reply(models.Model):
    comment_id = models.ForeignKey(Comment, default=1, on_delete=models.CASCADE)
    reply_content = models.CharField(max_length=500)
    likes = models.IntegerField()
    dislikes = models.IntegerField()