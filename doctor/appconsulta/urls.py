from django.urls import path
from .views import *

app_name = "atencion"
urlpatterns = [
    path('historia/', HistoriaView2.as_view(), name='historia'),
]