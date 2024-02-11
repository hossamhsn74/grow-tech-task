from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'published_on']
        read_only_fields = ['author', 'published_on']

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title must not be empty.")
        return value

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Content must not be empty.")
        return value

    def validate(self, data):
        if 'title' not in data or not data['title'].strip():
            raise serializers.ValidationError(
                {"title": "Title must not be empty."})
        if 'content' not in data or not data['content'].strip():
            raise serializers.ValidationError(
                {"content": "Content must not be empty."})
        return data
