from rest_framework.views import APIView, Request, Response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from users.permissions import IsAdmin
from .models import Dorama
from .serializers import DoramaSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema

class DoramaView(generics.ListAPIView):

    serializer_class = DoramaSerializer
    queryset = Dorama.objects.all()

class GetDoramaView(generics.ListAPIView):

        serializer_class = DoramaSerializer
        def get_queryset(self):

            dorama_id = self.kwargs["pk"]
            dorama_obj = get_object_or_404(Dorama, pk=dorama_id)
            dorama = Dorama.objects.filter(id=dorama_obj.id)

            return dorama

class CreateDoramaView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [ IsAuthenticated, IsAdmin ]
    
    @swagger_auto_schema(request_body=DoramaSerializer)
    def post(self, request: Request) -> Response:
            
            self.check_object_permissions(self.request, request.user)
            serializer = DoramaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status.HTTP_201_CREATED)

class DoramaDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [ IsAuthenticated, IsAdmin ]
        
    @swagger_auto_schema(request_body=DoramaSerializer)
    def patch(self, request: Request, pk: int) -> Response:

            self.check_object_permissions(self.request, request.user)
            dorama = get_object_or_404(Dorama, pk=pk)

            serializer = DoramaSerializer(dorama, request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:

            self.check_object_permissions(self.request, request.user)
            dorama = get_object_or_404(Dorama, pk=pk)
            dorama.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
