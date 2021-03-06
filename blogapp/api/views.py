from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from account.models import account
from blogapp.models import BlogPost
from blogapp.api.serializers import BlogPostSerializer

@api_view(['GET',])
def api_detail_blog_view(request, slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)

@api_view(['PUT',])
def api_detail_blog_view(request, slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = BlogPostSerializer(blog_post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data("sucess") == "Updated successfully"
            return Response(data=data)
        return Response(serializer.data)

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    