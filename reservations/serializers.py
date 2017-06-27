from .models import Evaluation
from rest_framework import serializers


class CommentsSerializer(serializers.HyperlinkedIdentityField):
    class Meta:
        model = Evaluation
        fields = ('id', 'opinion', 'seans', 'author', 'mark', 'timestamp')
