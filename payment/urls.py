from django.urls import path
from . import views
urlpatterns = [
    path('pay/', views.PaymentView.as_view(), name='pay'),
]