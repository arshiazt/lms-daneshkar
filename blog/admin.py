from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name','slug','description','is_active')
    list_filter = ('is_active',)
    search_fields = ('name','description')
    readonly_fields = ('slug',)

class ProductAdmin(admin.ModelAdmin):

    list_display = ('category','slug','price')
    list_editable = ('price',)
    fieldsets = (
        ('Name',{
            'fields':('category','slug')
        }),
        ('Price',{
            'fields':('price',)
        }
        ),
    )

admin.site.register(Product,ProductAdmin)