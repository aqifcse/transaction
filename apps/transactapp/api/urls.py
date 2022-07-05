from django.urls import path
from .views import TransactionAPIView

app_name = 'transactapp'

urlpatterns = [
    path('api/v1/transaction/', TransactionAPIView.as_view(), name='transaction')
]