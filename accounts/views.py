from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer

User = get_user_model()


class SignUp(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
