from rest_framework.decorators import api_view
from rest_framework.response import Response
from Team.models import TeamMember
from Team.serializers import TeamMemberSerializer

@api_view(['GET'])
def teamMemberAPI(request):
  team = TeamMember.objects.all()
  serializer = TeamMemberSerializer(team,many=True)
  return Response(serializer.data)