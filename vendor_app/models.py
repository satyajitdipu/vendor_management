from django.db import models
from django.db.models import Count, Avg
from django.utils import timezone
class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=255, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    delivery_date = models.DateTimeField(default=timezone.now)  # Default to current time
    po_number = models.CharField(max_length=255)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    issue_date = models.DateTimeField(default=None)  # Allow null values for historical data
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=255)
    quality_rating = models.FloatField(null=True, blank=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def calculate_on_time_delivery_rate(self):
        completed_pos = PurchaseOrder.objects.filter(
            vendor=self.vendor, status='completed'
        ).count()
        on_time_deliveries = PurchaseOrder.objects.filter(
            vendor=self.vendor, status='completed', delivery_date__lte=self.delivery_date
        ).count()

        if completed_pos == 0:
            return 0.0
        return (on_time_deliveries / completed_pos) * 100

    def calculate_quality_rating_avg(self):
        completed_pos_with_ratings = PurchaseOrder.objects.filter(
            vendor=self.vendor, status='completed', quality_rating__isnull=False
        )
        if completed_pos_with_ratings.count() == 0:
            return 0.0
        return completed_pos_with_ratings.aggregate(Avg('quality_rating'))['quality_rating__avg']

    def calculate_average_response_time(self):
        completed_pos_with_acknowledgment = PurchaseOrder.objects.filter(
            vendor=self.vendor, status='completed', acknowledgment_date__isnull=False
        )
        if completed_pos_with_acknowledgment.count() == 0:
            return 0.0
        total_response_time = sum(
            (po.acknowledgment_date - po.issue_date).total_seconds()
            for po in completed_pos_with_acknowledgment
        )
        return total_response_time / completed_pos_with_acknowledgment.count()

    def calculate_fulfillment_rate(self):
        total_pos = PurchaseOrder.objects.filter(vendor=self.vendor).count()
        successful_fulfillments = PurchaseOrder.objects.filter(
            vendor=self.vendor, status='completed', quality_rating__isnull=False
        ).count()
        if total_pos == 0:
            return 0.0
        return (successful_fulfillments / total_pos) * 100
    

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor} - {self.date}"
