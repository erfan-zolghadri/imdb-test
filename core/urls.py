from django.urls import path

from . import views

urlpatterns = [
    # path("test/", views.test_view, name="test"),
    path("sendmail/", views.send_mail_view, name="sendmail"),

    path("", views.MovieList.as_view(), name="movie-list"),
    path("<slug:slug>/", views.MovieDetail.as_view(), name="movie-detail"),
    path(
        "<slug:slug>/reviews/",
        views.ReviewCreate.as_view(),
        name="review-create",
    ),
]
