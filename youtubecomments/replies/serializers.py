from rest_framework import serializers
from .models import Reply

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['reply_id', 'comment_id', 'reply_content', 'likes', 'dislikes']