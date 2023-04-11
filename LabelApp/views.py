import logging

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Labels
from .serializer import LabelSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_labels(request):
    labels = Labels.objects.filter(user=request.user)
    serializer = LabelSerializer(labels, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_label(request, pk):
    try:
        label = Labels.objects.get(pk=pk, user=request.user)
        serializer = LabelSerializer(label)
        return Response(serializer.data)
    except Labels.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_label(request):
    serializer = LabelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_label(request, pk):
    try:
        label = Labels.objects.get(pk=pk, user=request.user)
    except Labels.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = LabelSerializer(label, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_label(request, pk):
    try:
        label = Labels.objects.get(pk=pk, user=request.user)
        label.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Labels.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
