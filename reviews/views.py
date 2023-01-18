from rest_framework.views import APIView, Request, Response, status

from doramas.models import Dorama
from users.models import User

from .models import Review
from .serializers import ReviewSerializer
from django.shortcuts import get_object_or_404

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class DoramaReviewView(APIView):

    #lists all reviews of a specifc Dorama
    def get(self, request: Request, pk: int) -> Response:
        dorama_review = Review.objects.filter(dorama_id=pk)
        serializer = ReviewSerializer(dorama_review, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class UserReviewView(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    #lists all reviews of a specifc user
    def get(self, request: Request, pk: int) -> Response:
        
        if request.user.id == pk:
            user_review = Review.objects.filter(user_id=pk)
            serializer = ReviewSerializer(user_review, many=True)

            return Response(serializer.data, status.HTTP_200_OK)
        return Response('You are not allowed to access others reviews.',status= status.HTTP_403_FORBIDDEN)
    
    def post(self, request: Request, pk: int) -> Response:
        
        dorama = get_object_or_404(Dorama, pk=pk)
        user = get_object_or_404(User, pk= request.user.id)
        
        serializer = ReviewSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(dorama_id = dorama, user_id = user)
            

        return Response(serializer.data, status.HTTP_201_CREATED)

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
        if request.user.is_admin == False:
            if review.user_id.id == request.user.id:
                review.delete()

                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response('You are not allowed to delete others reviews.',status= status.HTTP_403_FORBIDDEN)

        return Response(status=status.HTTP_204_NO_CONTENT)