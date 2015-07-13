from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Blog.models import Post
from Blog.serializers import PostSerializer,PostDetailSerializer

@api_view(['GET'])
def postAPI(request):
  post = Post.objects.all()
  serializer = PostSerializer(post,many=True)
  return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
def postAPIDetails(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)