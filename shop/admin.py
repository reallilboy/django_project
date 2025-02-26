from django.contrib import admin
from .models import Category,Product,Customer,Order
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)


class productAdmin(admin.ModelAdmin):
        fields =['name','category','publish_time']
        fieldsets =(
                ('content',{
                        'fields':('name','category')
                }),
                ('publishing',{
                        'fields':('publish_time'),
                        'classes':('collapse')
                })

        )
