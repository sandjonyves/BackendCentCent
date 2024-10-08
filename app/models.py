from django.db import models
from account.models import Etudiant
from store.models import Restaurant
import uuid
# Create your models here.

class Order(models.Model):
    # pk_comment  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    etudiant_id = models.ForeignKey(Etudiant,on_delete=models.CASCADE,related_name='order')
    restaurant_id = models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='order')
    # total_price = models.FloatField(  blank=True, default=0)
    order_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    operator = models.CharField(max_length = 256)
    dish_number = models.IntegerField()

class Payment(models.Model):
    payment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=[
        ('Card', 'Card'),
        ('Internal Balance', 'Internal Balance'),
    ])
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    status = models.CharField(max_length=20, choices=[
        ('Confirmed', 'Confirmed'),
        ('Pending', 'Pending'),
    ])

    def __str__(self):
        return f"Payment {self.payment_id} - {self.status}"
