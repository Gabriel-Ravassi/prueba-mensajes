from django.contrib import admin
from django.urls import path, include
from mensajes.views import lista_mensajes

urlpatterns = [
    path('admin/', admin.site.urls),

    # API para Expo
    path('api/', include('mensajes.urls')),

    # Página web para PC
    path('mensajes/', lista_mensajes),
]