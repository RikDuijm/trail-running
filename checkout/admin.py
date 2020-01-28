from django.contrib import admin
from .models import Order, OrderLineItem

# TabularInline subclass defines the template used to render the Order in the admin interface. StackedInline is another option.
# The Admin interface has the ability to edit more than one model on a single page. This is known as inlines.
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )

admin.site.register(Order, OrderAdmin)