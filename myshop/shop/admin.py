from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm
# Register your models here.
from .models import *



class ShoesProductAdmin(admin.ModelAdmin):


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug = "shoes"))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class TShirtsProductAdmin(admin.ModelAdmin):


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug = "tshirts"))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class HoodieProductProductAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug="hoodie"))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(ShoesProduct, ShoesProductAdmin)
admin.site.register(TShirtsProduct, TShirtsProductAdmin)
admin.site.register(HoodieProduct, HoodieProductProductAdmin)