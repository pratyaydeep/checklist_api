from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class TestAPIView(APIView):
    def get(self, request, format=None):
        return Response({'name': 'Pratyaydeep from Class Based View'})
