from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from . import models
from . import serializers


@permission_classes([IsAuthenticated])
class FriendViewSet(viewsets.ModelViewSet):
    queryset = models.Friend.objects.with_overdue()
    serializer_class = serializers.FriendSerializer


@permission_classes([IsAuthenticated])
class BelongingViewSet(viewsets.ModelViewSet):
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer


@permission_classes([IsAuthenticated])
class BorrowedViewSet(viewsets.ModelViewSet):
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer
    filterset_fields = {"returned": ["exact", "lte", "gte", "isnull"]}

    # Simple filtering
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     only_missing = str(self.request.query_params.get("missing")).lower()

    #     if only_missing in ["true", "1"]:
    #         return qs.filter(returned__isnull=True)

    #     return qs
