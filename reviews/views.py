import json
from rest_framework.views import APIView, Request, Response, status

from doramas.models import Dorama
from users.models import User
from users.serializers import UserSerializer

from .models import Review
from .serializers import ReviewSerializer
from django.shortcuts import get_object_or_404


class DoramaReviewView(APIView):

    #lists all reviews of a specifc Dorama
    def get(self, request: Request, pk: int) -> Response:
        dorama_review = Review.objects.filter(dorama_id=pk)
        serializer = ReviewSerializer(dorama_review, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class UserReviewView(APIView):
    def post(self, request: Request, pk: int) -> Response:
        
        dorama = get_object_or_404(Dorama, pk=pk)
        user = get_object_or_404(User, pk=pk)
        # user = UserSerializer(request.user)
        
        serializer = ReviewSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(dorama_id = dorama, user_id = user)
            

        return Response(serializer.data, status.HTTP_201_CREATED)

    #lists all reviews of a specifc user
    def get(self, request: Request, pk: int) -> Response:
        user_review = Review.objects.filter(user_id=pk)
        serializer = ReviewSerializer(user_review, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, pk: int) -> Response:
        review = get_object_or_404(Review, pk=pk)

        serializer = ReviewSerializer(review, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        review = get_object_or_404(Review, pk=pk)
        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)