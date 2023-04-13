from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserResponseSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import AppUsers
from .serializers import UserSerializer


@api_view(['GET'])
def user_list(request):
    users = AppUsers.objects.all()
    serializer = UserResponseSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_detail(request, id):
    user = AppUsers.objects.get(id=id)
    serializer = UserResponseSerializer(user)
    return Response(serializer.data)


@api_view(['PUT'])
def user_update(request, id):
    user = AppUsers.objects.get(id=id)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def user_delete(request, id):
    user = AppUsers.objects.get(id=id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def user_list_by_team(request, team_id):
    users = AppUsers.objects.filter(team__id=team_id)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
