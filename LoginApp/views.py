
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
import logging

class CustomTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        # Do your custom business logic here
        logging.info(f"Request Data: {request.data}")
        response = super().post(request, *args, **kwargs)
        # Do some more custom business logic here
        return response
