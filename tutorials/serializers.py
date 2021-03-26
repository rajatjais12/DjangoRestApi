
from tutorials.models import song
from rest_framework import serializers
 
 
class songSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = song
        fields = ('Id',
                  'name_of_song',
                  'duration',
                  'published')
