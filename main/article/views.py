from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework import generics, status
from .permissions import IsOwnerOrReadOnly, IsOwnerOnly
from rest_framework.authentication import TokenAuthentication


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleListSerializer
    queryset = Article.objects.all()


class ArticleCreateView(generics.CreateAPIView):
    serializer_class = ArticleCreateSerializer
    queryset = Article.objects.all()


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleDetailSerializer
    queryset = Article.objects.all()


class UserProfileView(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (IsOwnerOnly, )
    lookup_field = 'pk'

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)


def articles_app(request):
    return render(request, 'index.html')



