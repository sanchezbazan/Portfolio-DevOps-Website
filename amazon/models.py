from django.db import models

class AWSCostQuery(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    granularity = models.CharField(max_length=10, choices=[('DAILY', 'Daily'), ('MONTHLY', 'Monthly')])

    def __str__(self):
        return f"{self.start_date} to {self.end_date} - {self.granularity}"

class AWSCostData(models.Model):
    query = models.ForeignKey(AWSCostQuery, on_delete=models.CASCADE, related_name='cost_data')
    date = models.DateField()
    service = models.CharField(max_length=100)
    environment = models.CharField(max_length=100, null=True, blank=True)
    blended_cost = models.DecimalField(max_digits=10, decimal_places=2)
    unblended_cost = models.DecimalField(max_digits=10, decimal_places=2)
    usage_quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.service}"
