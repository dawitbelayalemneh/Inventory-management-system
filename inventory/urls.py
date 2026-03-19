from django.urls import path
from .views import index, display_laptops, display_desktops, display_mobiles # make sure these exist

urlpatterns = [
    path('', index, name='index'),
    path('laptops/', display_laptops, name='display_laptops'),
    path('desktops/', display_desktops, name='display_desktops'),
    path('mobiles/', display_mobiles, name='display_mobiles'),
]