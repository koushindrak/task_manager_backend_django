import logging

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import TeamSerializer

from .models import Teams


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_teams(request):
    logging.info("######## Getting All Teams")
    teams = Teams.objects.filter(users=request.user)
    serializer = TeamSerializer(teams, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_team(request, pk):
    logging.info("######## Getting Team by id {pk}")

    try:
        team = Teams.objects.get(pk=pk, users=request.user)
    except Teams.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TeamSerializer(team)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_team(request):
    logging.info(f"######## Creating Team:  {request}")

    serializer = TeamSerializer(data=request.data, context={'user': request.user})
    if serializer.is_valid():
        team = serializer.save(created_by=request.user.username, updated_by=request.user.username)
        team.users.add(request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_team(request, pk):
    logging.info(f"######## Updating Team:  {request} ----  {pk}")

    try:
        team = Teams.objects.get(pk=pk, users=request.user)
    except Teams.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TeamSerializer(team, data=request.data,context={'user': request.user})
    if serializer.is_valid():
        team = serializer.save(created_by=request.user.username, updated_by=request.user.username)
        team.users.add(request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_team(request, pk):
    logging.info(f"######## Deleting Team:  {request}  ---- {pk}")
    try:
        team = Teams.objects.get(pk=pk, users=request.user)
    except Teams.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    team.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
