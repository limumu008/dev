
from django.db import models
from django.utils import timezone


class Provider(models.Model):
    provider_id = models.AutoField(primary_key=True)
    provider_name = models.CharField(max_length=50, unique=True)
    provider_email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=10)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)

    def __str__(self):
        return (self.provider_name)


class Kitchen(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    kitchen_id = models.Autofield(primary_key=True)
    kitchen_pic = models.ImageField()


    Mon = model.BooleanField(default=False)
    Tue = model.BooleanField(default=False)
    Wed = model.BooleanField(default=False)
    Thur = model.BooleanField(default=False)
    Fri = model.BooleanField(default=False)
    Sat = model.BooleanField(default=False)
    Sun = model.BooleanField(default=False)


    start_time_choices = (
        (6,'6 AM'),
        (7,'7 AM'),
        (8,'8 AM'),
        (9,'9 AM'),
        (10,'10 AM'),
        (11,'11 AM'),
        (12,'12 PM'),
        (13,'1 PM'),
        (14,'2 PM'),
        (15,'3 PM'),
        (16,'4 PM'),
        (17,'5 PM'),
        (18,'6 PM'),

    )
    start_time = models.PositiveSmallIntegerField(
                                      choices=start_time_choices,
                                      default=9)

    end_time_choices = (

        (11, '11 AM'),
        (12, '12 PM'),
        (13, '1 PM'),
        (14, '2 PM'),
        (15, '3 PM'),
        (16, '4 PM'),
        (17, '5 PM'),
        (18, '6 PM'),
        (19, '7 PM'),
        (20, '8 PM'),
        (21, '9 PM'),
        (22, '10 PM'),
        (23, '11 PM'),

    )
    end_time = models.PositiveSmallIntegerField(
                                                  choices=end_time_choices,
                                                  default=17)

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

class Menu(models.Model):
    meal_id = models.Autofield(primary_key=True)
    meal = model.CharField(max_length=50, unique=True)
    vegetarian = model.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    kitchen = models.ForeignKey(Kitchen,on_delete=models.CASCADE)

    def __str__(self):
        return (self.meal)