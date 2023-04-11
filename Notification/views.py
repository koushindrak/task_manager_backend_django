import logging
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import NotificationSerializer
from .models import Notifications


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_notifications(request):
    logging.info("######## Getting All Notifications")
    notifications = Notifications.objects.filter(user=request.user)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notification(request, pk):
    logging.info("######## Getting Notification by id {pk}")
    try:
        notification = Notifications.objects.get(pk=pk, user=request.user)
    except Notifications.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NotificationSerializer(notification)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_notification(request):
    logging.info(f"######## Creating Notification:  {request}")
    serializer = NotificationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_notification(request, pk):
    logging.info(f"######## Updating Notification:  {request} ----  {pk}")
    try:
        notification = Notifications.objects.get(pk=pk, user=request.user)
    except Notifications.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = NotificationSerializer(notification, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_notification(request, pk):
    logging.info(f"######## Deleting Notification:  {request}  ---- {pk}")
    try:
        notification = Notifications.objects.get(pk=pk, user=request.user)
    except Notifications.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    notification.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
