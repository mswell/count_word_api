from rest_framework import serializers


class CountSerializer(serializers.Serializer):
    url = serializers.URLField()
    word = serializers.CharField(max_length=100)
