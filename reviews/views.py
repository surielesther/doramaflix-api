from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from doramas.models import Dorama
from .models import Review
from .serializers import ReviewSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema


class DoramaReviewView(generics.ListAPIView):

    #lists all reviews of a specifc Dorama
    serializer_class = ReviewSerializer

    def get_queryset(self):
        dorama_id = self.kwargs["pk"]
        review = Review.objects.filter(dorama_id=dorama_id)

        return review

class GetUserReview(generics.ListAPIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
   
    #lists all reviews of a specifc user
    def get_queryset(self):
        user_id = self.request.user.id
        reviews = Review.objects.filter(user_id=user_id)

        return reviews
    
class UserReviewView(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(request_body=ReviewSerializer)
    def post(self, request: Request, pk: int) -> Response:
        
        dorama = get_object_or_404(Dorama, pk=pk)
        user = request.user
        serializer = ReviewSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(dorama_id = dorama, user_id = user)

        return Response(serializer.data, status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=ReviewSerializer)
    def patch(self, request: Request, pk: int) -> Response:
        review = get_object_or_404(Review, pk=pk)
        
        if review.user_id.id == request.user.id:
            serializer = ReviewSerializer(review, request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response('You are not allowed to update others reviews.',status= status.HTTP_403_FORBIDDEN)

    def delete(self, request: Request, pk: int) -> Response:
        review = get_object_or_404(Review, pk=pk)

        if review.user_id.id == request.user.id:
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response('You are not allowed to delete others reviews.',status= status.HTTP_403_FORBIDDEN)