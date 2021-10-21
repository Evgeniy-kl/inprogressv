from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('articles/', ArticleListView.as_view()),
    path('articles/create', ArticleCreateView.as_view()),
    path('articles/<int:pk>', ArticleDetailView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('articles_page/', articles_app),
]
