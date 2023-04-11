import logging

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProjectSerializer

from .models import Projects


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_projects(request):
    logging.info("######## Getting All Project")
    projects = Projects.objects.filter(user=request.user)
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_project(request, pk):
    logging.info("######## Getting Project by id {pk}")

    try:
        project = Projects.objects.get(pk=pk, user=request.user)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProjectSerializer(project)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):
    logging.info(f"######## Creating Project:  {request}")

    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_project(request, pk):
    logging.info(f"######## updating Project:  {request} ----  {pk}")

    try:
        project = Projects.objects.get(pk=pk, user=request.user)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProjectSerializer(project, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_project(request, pk):
    logging.info(f"######## Deleting Project:  {request}  ---- {pk}")
    try:
        project = Projects.objects.get(pk=pk, user=request.user)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    project.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
