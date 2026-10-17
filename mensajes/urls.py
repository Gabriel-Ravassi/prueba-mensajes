from django.urls import path
from .views import MensajeListCreateView

urlpatterns = [
    path('mensajes/', MensajeListCreateView.as_view()),
]