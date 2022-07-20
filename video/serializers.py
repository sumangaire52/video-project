from rest_framework import serializers

from .models import Video
from .validators import validate_video

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    video = serializers.FileField(validators = [validate_video])
    class Meta:
        model = Video
        fields = ['id','title','video']

class CostingSerializer(serializers.Serializer):
    size = serializers.IntegerField(min_value=1, max_value=1024)
    duration = serializers.IntegerField(min_value=1, max_value=36000)
    type = serializers.ChoiceField(choices = ['mp4','mkv'])