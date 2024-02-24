from django.urls import path
from .views import *


urlpatterns = [
    path('', post_index, name='post-index'),  # /posts: shows
]
