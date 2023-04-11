import logging
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer
from .models import Comments


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_comments(request):
    logging.info("######## Getting All Comments")
    comments = Comments.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_comment(request, pk):
    logging.info(f"######## Getting Comment by id {pk}")
    try:
        comment = Comments.objects.get(pk=pk)
    except Comments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CommentSerializer(comment)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request):
    logging.info(f"######## Creating Comment:  {request}")
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_comment(request, pk):
    logging.info(f"######## Updating Comment:  {request} ----  {pk}")
    try:
        comment = Comments.objects.get(pk=pk)
    except Comments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request, pk):
    logging.info(f"######## Deleting Comment:  {request}  ---- {pk}")
    try:
        comment = Comments.objects.get(pk=pk)
    except Comments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
