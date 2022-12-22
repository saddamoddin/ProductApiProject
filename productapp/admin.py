from django.contrib import admin
from .models import ProductModel , ComapanyModel

# Register your models here.
class adminProduct(admin.ModelAdmin):
    list_display = ['id','name','price','description','category']
admin.site.register(ProductModel,adminProduct)

class companyDetails(admin.ModelAdmin):
    list_display = ['id','name','bio']
admin.site.register(ComapanyModel,companyDetails)