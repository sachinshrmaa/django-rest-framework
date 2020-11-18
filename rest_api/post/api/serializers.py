from rest_framework import serializers

from post.models import Post


class PostSerializer(serializers.ModelSerializer):
    '''
    Model Serializer for our Post model.
    '''
    class Meta:
        model = Post
        fields = '__all__'
    