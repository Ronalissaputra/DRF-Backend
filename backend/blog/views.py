from rest_framework import generics
from .models import Author, Blog
from .serializers import AuthorSerializer, BlogSerializer


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogByauthorListView(generics.ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        author_id = self.kwargs["author_id"]
        return Blog.objects.filter(author_id=author_id)
