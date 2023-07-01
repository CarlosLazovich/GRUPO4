from django.urls import path, include
from core import views



urlpatterns = [
    path('index/', views.indexView, name = 'index'),

    # includes
    path('publicaciones/', include('publicaciones.urls')),
    path('usuarios/', include('usuarios.urls'))
]


