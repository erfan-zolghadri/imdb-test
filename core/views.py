from django.db.models import Avg
from django.http.response import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from .tasks import send_mail_func


# def test_view(request):
#     test_func.delay()
#     return HttpResponse("Done")


def send_mail_view(request):
    send_mail_func.delay()
    return HttpResponse("Emails were sent")


class MovieList(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.active_movies.annotate(ratings_avg=Avg("reviews__rating"))


class MovieDetail(generics.RetrieveAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.active_movies.annotate(ratings_avg=Avg("reviews__rating"))
    lookup_field = "slug"


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        movie_slug = self.kwargs.get("slug")
        user = self.request.user

        context.update({"movie_slug": movie_slug, "user": user})

        return context
