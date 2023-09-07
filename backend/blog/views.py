from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .models import Author, Blog
from .serializers import AuthorSerializer, BlogSerializer


class BlogListPagination(PageNumberPagination):
    page_size = 10


@api_view(["GET", "POST"])
def Blog_list(request):
    if request.method == "GET":
        paginator = BlogListPagination()
        blogs = Blog.objects.all()
        result_page = paginator.paginate_queryset(blogs, request)
        serializer = BlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    elif request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def Blog_detail(request, id):
    try:
        blogs = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BlogSerializer(blogs)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = BlogSerializer(blogs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        blogs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
