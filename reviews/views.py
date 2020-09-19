from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # anytime someone saves a review just before is saved
    # the code grabs whatever user made this API call and
    # will set that as the poster

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
