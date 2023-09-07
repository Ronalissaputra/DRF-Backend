from django.urls import path
from . import views

urlpatterns = [
    path("blogs/", views.Blog_list, name="blog-list"),
    path("blog/<int:id>/", views.Blog_detail, name="blog-detail"),
]
