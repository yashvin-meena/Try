from django.urls import path
from .views import StaticAPIView, PlayerAPIView

urlpatterns = [
   path('', StaticAPIView.as_view(), name='static'),
   path('player/', PlayerAPIView.as_view(), name='player')
]