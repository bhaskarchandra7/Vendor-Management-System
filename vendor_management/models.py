from django.db import models
from django.db.models import Avg, F

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def calculate_on_time_delivery_rate(self):
        completed_orders_count = self.purchase_orders.filter(status='completed').count()
        if completed_orders_count == 0:
            return 0
        on_time_orders_count = self.purchase_orders.filter(status='completed', delivery_date__lte=F('acknowledgment_date')).count()
        return (on_time_orders_count / completed_orders_count) * 100
    
    def calculate_quality_rating_avg(self):
        return self.purchase_orders.filter(status='completed').aggregate(avg_quality=Avg('quality_rating'))['avg_quality'] or 0
    
    def calculate_average_response_time(self):
        response_times = self.purchase_orders.filter(status='completed', acknowledgment_date__isnull=False).annotate(
            response_time=models.F('acknowledgment_date') - models.F('issue_date')
        ).aggregate(avg_response=Avg('response_time'))['avg_response']
        return response_times.total_seconds() / len(response_times) if response_times else 0
    
    def calculate_fulfillment_rate(self):
        total_orders_count = self.purchase_orders.count()
        if total_orders_count == 0:
            return 0
        fulfilled_orders_count = self.purchase_orders.filter(status='completed').count()
        return (fulfilled_orders_count / total_orders_count) * 100

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_orders')
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.vendor.on_time_delivery_rate = self.vendor.calculate_on_time_delivery_rate()
        self.vendor.quality_rating_avg = self.vendor.calculate_quality_rating_avg()
        self.vendor.average_response_time = self.vendor.calculate_average_response_time()
        self.vendor.fulfillment_rate = self.vendor.calculate_fulfillment_rate()
        self.vendor.save()

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
