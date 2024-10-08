
from django.db import models
# from account.models  import Admin
from asgiref.sync import sync_to_async
# Create your models here.


class Restaurant(models.Model):
    # admin = models.OneToOneField(Admin,on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Restaurant {self.id}"

class Dish(models.Model):
    restaurant_id = models.ManyToManyField(Restaurant,related_name='dish')
    name =  models.CharField(max_length=255,blank=True,default='')
    food_number = models.IntegerField(verbose_name='max food number of one day ')
    dish_max_number = models.IntegerField(verbose_name='max dish that student command ')
    proteine = models.CharField(max_length=32,blank=True,default='',null=True)
    fruit = models.CharField(max_length=32,blank=True,default='',null=True)
    # obstacle = models.CharField(max_length=32,blank=True,default='')
    is_choise = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    @classmethod
    @sync_to_async
    def get_choise(cls):
        return list(cls.objects.filter(is_choise=True).values('id', 'name'))  # Retourne une liste de dictionnaires    
    
class Proteine(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
    
class Fruit(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name