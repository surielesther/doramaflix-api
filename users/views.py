from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404


class RegisterView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LoginView(TokenObtainPairView):
    ...


class UserDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, pk: int) -> Response:

        if request.user.id == pk:
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(user)

            return Response(serializer.data, status.HTTP_200_OK)
        return Response('You are not allowed to access others profiles.',status= status.HTTP_403_FORBIDDEN)

    def patch(self, request: Request, pk: int) -> Response:
        if request.user.id == pk:
            user = get_object_or_404(User, pk=pk)

            serializer = UserSerializer(user, request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status.HTTP_200_OK)
        return Response('You are not allowed to access update profiles.',status= status.HTTP_403_FORBIDDEN)


    def delete(self, request: Request, pk: int) -> Response:
        if request.user.id == pk:
            user = get_object_or_404(User, pk=pk)
            user.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response('You are not allowed to access delete profiles.',status= status.HTTP_403_FORBIDDEN)
