import logging

from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    logging.info(exc)
    """
    Custom exception handler that returns a formatted error response.
    """
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # If the response is None, an unhandled exception occurred.
    if response is None:
        error_message = 'Sorry !!! Something went wrong,'
        error_message += ' Please try again later.'
        return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Customize the error response.
    error_message = 'An error occurred while processing your request.'
    error_message += ' Please check the data and try again.'

    response.data = {'error': error_message}

    return response
