from rest_framework import serializers
from apps.transactapp.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['sent_from', 'sent_to', 'sent_at', 'amount_sent']