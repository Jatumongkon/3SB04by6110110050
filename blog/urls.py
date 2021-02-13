from django.urls import path
from . import views
from . import urls

urlpatterns = [
    path('', views.post_list),
    path('tab',views.tab)
]