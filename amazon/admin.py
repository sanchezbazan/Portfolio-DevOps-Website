from django.contrib import admin
from .models import AWSCostQuery, AWSCostData
from .views import AWSCostQueryViewSet
from .services import fetch_and_store_aws_data

class AWSCostDataInline(admin.TabularInline):
    model = AWSCostData
    extra = 0
    readonly_fields = ('date', 'service', 'environment', 'blended_cost', 'unblended_cost', 'usage_quantity')
    can_delete = False

@admin.register(AWSCostQuery)
class AWSCostQueryAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'granularity', 'cost_data_count')
    inlines = [AWSCostDataInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # This ensures the instance is saved before fetching AWS data
        self.fetch_and_store_aws_data(obj)

    def fetch_and_store_aws_data(self, query):
        # You can refactor this to avoid directly using the viewset method if needed
        viewset_instance = fetch_and_store_aws_data(query)

    def cost_data_count(self, obj):
        return obj.cost_data.count()
    cost_data_count.short_description = 'Cost Data Records'

@admin.register(AWSCostData)
class AWSCostDataAdmin(admin.ModelAdmin):
    list_display = ('query', 'date', 'service', 'environment', 'blended_cost', 'unblended_cost', 'usage_quantity')
    readonly_fields = ('query', 'date', 'service', 'environment', 'blended_cost', 'unblended_cost', 'usage_quantity')
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
