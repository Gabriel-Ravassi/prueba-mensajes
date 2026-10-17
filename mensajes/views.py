from django.shortcuts import render
from rest_framework import generics
from .models import Mensaje
from .serializers import MensajeSerializer


class MensajeListCreateView(generics.ListCreateAPIView):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer


def lista_mensajes(request):
    mensajes = Mensaje.objects.all()
    return render(request, 'mensajes/lista.html', {'mensajes': mensajes})