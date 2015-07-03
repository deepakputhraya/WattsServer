from rest_framework import serializers
from Animal.models import Animal,Adopt,Story

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('name','breed','image')

class AdoptSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    class Meta:
        model = Adopt
        fields = ('animal','description')



class StorySerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    class Meta:
        model = Adopt
        fields = ('animal','description')
