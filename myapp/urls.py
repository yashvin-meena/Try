from django.urls import path
from .views import StaticAPIView

urlpatterns = [
   path('', StaticAPIView.as_view(), name='static')
]