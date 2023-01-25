from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import User
from .permissions import IsAdmin
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
import ipdb


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class LoginView(TokenObtainPairView):
    ...
    
class ListUsersView(generics.ListAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin] 

    serializer_class = UserSerializer
    def get_queryset(self):

            user = User.objects.all()
            self.check_object_permissions(self.request, user)
            return user

class GetProfileView(generics.ListAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        user = User.objects.filter(id=user_id)

        return user

class UserView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=UserSerializer)
    def patch(self, request: Request) -> Response:
        
            user = get_object_or_404(User, pk=request.user.id)

            serializer = UserSerializer(user, request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request) -> Response:
        
            user = get_object_or_404(User, pk=request.user.id)
            user.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
