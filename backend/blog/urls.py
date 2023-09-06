from django.urls import path
from . import views

urlpatterns = [
    path("authors/", views.AuthorListCreateView.as_view(), name="author-list-create"),
    path("blogs/", views.BlogListCreateView.as_view(), name="blog-list-create"),
    path(
        "blogs/author/<int:author_id>/",
        views.BlogByauthorListView.as_view(),
        name="blog-by-author",
    ),
]
