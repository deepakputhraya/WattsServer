from rest_framework import serializers
from Blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','description')


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post