from rest_framework.views import APIView, Request, Response, status

from .models import Dorama
from .serializers import DoramaSerializer
from django.shortcuts import get_object_or_404


class DoramaView(APIView):
    def get(self, request: Request) -> Response:
        doramas = Dorama.objects.all()
        serializer = DoramaSerializer(doramas, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = DoramaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class DoramaDetailView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        dorama = get_object_or_404(Dorama, pk=pk)
        serializer = DoramaSerializer(dorama)

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, pk: int) -> Response:
        dorama = get_object_or_404(Dorama, pk=pk)

        serializer = DoramaSerializer(dorama, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        dorama = get_object_or_404(Dorama, pk=pk)
        dorama.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)