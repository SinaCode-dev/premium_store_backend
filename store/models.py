from django.conf import settings
from django.db import models

from uuid import uuid4
from phonenumber_field.modelfields import PhoneNumberField



class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        region = "IR",
        unique=True,
        blank=False,
        null=False,
        verbose_name="Phone number",
        help_text="Iranian format phone number(example: 09123456789)",
    )


class Application(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    top_service = models.ForeignKey('Service', null=True, blank=True, on_delete=models.SET_NULL, related_name='applications')


class Discount(models.Model):
    discount_percent = models.FloatField()
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=250)


class Service(models.Model):
    name = models.CharField(max_length=250)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='services')
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    discounts = models.ForeignKey(Discount, null=True, blank=True, on_delete=models.SET_NULL)


class Comment(models.Model):
    COMMENT_STATUS_WAITING = 'w'
    COMMENT_STATUS_APPROVED = 'a'
    COMMENT_STATUS_NOT_APPROVED = 'na'
    COMMENT_STATUS = [
        (COMMENT_STATUS_WAITING, 'Waiting'),
        (COMMENT_STATUS_APPROVED, 'Approved'),
        (COMMENT_STATUS_NOT_APPROVED, 'Not Approved'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    status = models.CharField(max_length=2, choices=COMMENT_STATUS, default=COMMENT_STATUS_WAITING)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    datetime_created = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


class Order(models.Model):
    ORDER_STATUS_PAID = 'p'
    ORDER_STATUS_UNPAID = 'u'
    ORDER_STATUS_CANCELED = 'c'
    ORDER_STATUS = [
        (ORDER_STATUS_PAID,'Paid'),
        (ORDER_STATUS_UNPAID,'Unpaid'),
        (ORDER_STATUS_CANCELED,'Canceled'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    datetime_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=ORDER_STATUS, default=ORDER_STATUS_UNPAID)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="items")
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=5, decimal_places=2)