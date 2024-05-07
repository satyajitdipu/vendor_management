from django.shortcuts import render
from .models import Vendor, PurchaseOrder
from rest_framework import viewsets
from .serializers import VendorSerializer, PurchaseOrderSerializer
from rest_framework.response import Response
from django.db.models import Count, Avg,F,Sum
# Create your views here.
class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
class VendorPerformanceViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        
        vendor = Vendor.objects.get(pk=pk)
        completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        total_pos = PurchaseOrder.objects.filter(vendor=vendor)

        on_time_delivery_rate = completed_pos.filter(delivery_date__lte=F('issue_date')).count() / completed_pos.count() if completed_pos.count() > 0 else 0.0
        quality_rating_avg = completed_pos.aggregate(avg_quality=Avg('quality_rating'))['avg_quality'] if completed_pos.count() > 0 else 0.0

        # Calculate the sum of response times for all completed POs
        total_response_time = completed_pos.aggregate(sum_response=Sum(F('acknowledgment_date') - F('issue_date')))['sum_response']
        # Calculate the average response time if there are completed POs
        avg_response_time = total_response_time.total_seconds() / completed_pos.count() if completed_pos.count() > 0 else 0.0

        fulfillment_rate = completed_pos.count() / total_pos.count() if total_pos.count() > 0 else 0.0

        return Response({
            'on_time_delivery_rate': on_time_delivery_rate,
            'quality_rating_avg': quality_rating_avg,
            'avg_response_time': avg_response_time,
            'fulfillment_rate': fulfillment_rate
        })
