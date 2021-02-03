from django.urls import path
from . import views
from . import urls

urlpatterns = [
    path('', views.post_list, name='post_list'),
]