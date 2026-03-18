from django.urls import path
from .views import index   # make sure this exists

urlpatterns = [
    path('', index, name='index'),
]