import logging
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer, TaskResponseSerializer, TaskRequestSerializer, TaskResponseSerializer2
from .models import Tasks


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_tasks(request):
    logging.info("######## Getting All Tasks")
    tasks = Tasks.objects.filter(user=request.user)
    serializer = TaskResponseSerializer2(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_task(request, pk):
    logging.info("######## Getting Task by id {pk}")
    try:
        task = Tasks.objects.get(pk=pk, user=request.user)
    except Tasks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskResponseSerializer(task)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    serializer = TaskRequestSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task(request, pk):
    logging.info(f"######## Updating Task:  {request} ----  {pk}")
    try:
        task = Tasks.objects.get(pk=pk, user=request.user)
    except Tasks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskRequestSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, pk):
    logging.info(f"######## Deleting Task:  {request}  ---- {pk}")
    try:
        task = Tasks.objects.get(pk=pk, user=request.user)
    except Tasks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
