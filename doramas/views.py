from rest_framework.views import APIView, Request, Response, status

from .models import Dorama
from .serializers import DoramaSerializer
from django.shortcuts import get_object_or_404

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics


class DoramaView(generics.ListAPIView):

    serializer_class = DoramaSerializer
    queryset = Dorama.objects.all()

class GetDoramaView(APIView):

    def get(self, request: Request, pk: int) -> Response:
        dorama = get_object_or_404(Dorama, pk=pk)
        serializer = DoramaSerializer(dorama)

        return Response(serializer.data, status.HTTP_201_CREATED)


class CreateDoramaView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [ IsAuthenticated ]
    
    def post(self, request: Request) -> Response:
        if request.user.is_admin == True:
            serializer = DoramaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.save()

            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response('Common users are not allowed to post a dorama.',status= status.HTTP_403_FORBIDDEN)


class DoramaDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [ IsAuthenticated ]

        
    def patch(self, request: Request, pk: int) -> Response:
        if request.user.is_admin == True:
            dorama = get_object_or_404(Dorama, pk=pk)

            serializer = DoramaSerializer(dorama, request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status.HTTP_200_OK)
        return Response('Common users are not allowed to post a dorama.',status= status.HTTP_403_FORBIDDEN)

    def delete(self, request: Request, pk: int) -> Response:
        if request.user.is_admin == True:
            dorama = get_object_or_404(Dorama, pk=pk)
            dorama.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response('Common users are not allowed to post a dorama.',status= status.HTTP_403_FORBIDDEN)
