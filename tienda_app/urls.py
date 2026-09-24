from django.urls import path
from tienda_app.api.views import CompraAPIView

urlpatterns = [
    path('api/v1/comprar/', CompraAPIView.as_view(), name='api_comprar'),
]
