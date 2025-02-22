from django.contrib import admin
from .models import Category, Product, Slider, About, Offer, Client, ContactInfo, Reservation
from django.utils.safestring import mark_safe


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo_img_tag', 'price', 'category', 'is_visible', 'sort')
    list_display_links = ('id', 'name')
    list_editable = ('price', 'category', 'is_visible', 'sort')
    list_filter = ('category', 'is_visible')
    search_fields = ('name',)

    def photo_img_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='50'>")

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'is_visible', 'sort')
    list_display_links = ('id', 'name')
    list_editable = ('text', 'is_visible', 'sort')
    list_filter = ('is_visible', 'sort')
    search_fields = ('name',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'is_visible', 'sort')
    list_display_links = ('id', 'name')
    list_editable = ('text', 'is_visible', 'sort')
    list_filter = ('is_visible', 'sort')
    search_fields = ('name',)

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo_img_tag', 'percent', 'status', 'is_visible', 'sort')
    list_display_links = ('id', 'name')
    list_editable = ('percent', 'status', 'is_visible', 'sort')
    list_filter = ('is_visible', 'sort')
    search_fields = ('name',)

    def photo_img_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='50'>")

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo_img_tag', 'text', 'grade', 'is_visible', 'sort')
    list_display_links = ('id', 'name')
    list_editable = ('text', 'grade', 'is_visible', 'sort')
    list_filter = ('is_visible', 'sort')
    search_fields = ('name',)

    def photo_img_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='50'>")

class ProductInline(admin.StackedInline):
    model = Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline,]

# Register your models here.
admin.site.register(ContactInfo)
admin.site.register(Reservation)