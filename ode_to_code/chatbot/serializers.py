from rest_framework import serializers

class requestSerializer(serializers.Serializer):
    question_key = serializers.CharField()
    options = serializers.ListField()
    audio = serializers.FileField()