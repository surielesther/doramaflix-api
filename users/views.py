from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404

class RegisterView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    ...


class UserDetailView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, pk: int) -> Response:
        user = get_object_or_404(User, pk=pk)

        serializer = UserSerializer(user, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        user = get_object_or_404(User, pk=pk)
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)