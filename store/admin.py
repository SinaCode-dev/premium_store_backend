from django.contrib import admin
from .models import Customer, Application, Discount, Service, Comment, Cart, CartItem, Order, OrderItem


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["user", "phone_number"]


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "top_service"]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ["discount_percent", "code", "name"]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "application", "description", "price", "datetime_created", "discounts"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["author", "service", "body", "status", "datetime_created"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "datetime_created"]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ["cart", "service"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "datetime_created", "status"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "service", "price"]