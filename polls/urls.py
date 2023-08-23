from .views import balls, boots, t_shirts
from django.urls import path

urlpatterns = [
    path('t_shirt/', t_shirts),
    path('boot/', boots),
    path('ball/', balls)
]