from django.urls import path
from .views import home, remover, about, contact, privaypolicy, termsandconditions
urlpatterns = [
    path('', home, name='homepage'),
    path('about/', about, name='aboutpage'),
    path('contact/', contact, name='contactpage'),
    path('privacy-policy/', privaypolicy, name='privacypolicypage'),
    path('terms-and-conditions/', termsandconditions, name='termsandconditionspage'),
    path('remove/', remover, name='remover'),
]
