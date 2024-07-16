from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('create-checkout-session/<int:id>', views.create_checkout_session, name='create_checkout_session'),

    path('sucesso/', views.sucesso, name='sucesso'),

    path('erro/', views.erro, name='erro'),

    path('stripe_webhook', views.stripe_webhook, name='stripe_webhook'),
]
