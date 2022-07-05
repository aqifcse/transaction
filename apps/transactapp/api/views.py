from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TransactionSerializer
from apps.transactapp.models import Transaction


class TransactionAPIView(APIView):
    """
    List all transactions, or create a new snippet.
    """
    def get(self, request, format=None):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)