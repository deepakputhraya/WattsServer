from rest_framework.decorators import api_view
from rest_framework.response import Response
from Animal.models import Animal,Adopt,Story
from Animal.serializers import AnimalSerializer,AdoptSerializer,StorySerializer

@api_view(['GET'])
def animalAPI(request):
  animal = Animal.objects.all()
  serializer = AnimalSerializer(animal,many=True)
  return Response(serializer.data)


@api_view(['GET'])
def adoptAPI(request):
  adopt = Adopt.objects.all()
  serializer = AdoptSerializer(adopt,many=True)
  return Response(serializer.data)


@api_view(['GET'])
def storyAPI(request):
  story = Story.objects.all()
  serializer = StorySerializer(story,many=True)
  return Response(serializer.data)