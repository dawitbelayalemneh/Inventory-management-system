from django.urls import path
from .views import index, display_laptops, display_desktops, display_mobiles, add_laptop, add_desktop, add_mobile

urlpatterns = [
    path('', index, name='index'),
    path('laptops/', display_laptops, name='display_laptops'),
    path('desktops/', display_desktops, name='display_desktops'),
    path('mobiles/', display_mobiles, name='display_mobiles'),

    path('add_laptops/', add_laptop, name='add_laptop'),
    path('add_desktops/', add_desktop, name='add_desktop'),
    path('add_mobiles/', add_mobile, name='add_mobile'),
]