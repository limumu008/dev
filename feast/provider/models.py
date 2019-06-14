
from django.db import models
from django.utils import timezone


class Provider(models.Model):
    provider_id = models.AutoField(primary_key=True)
    provider_name = models.CharField(max_length=50, unique=True)
    provider_email = models.CharField(max_length=50, unique=True)
    provider_password = models.CharField(max_length=10)
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE)

    def __str__(self):
        return (self.provider_name)


class Kitchen(models.Model):

    kitchen_id = models.Autofield(primary_key=True)
    kitchen_pic = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)


    Mon = models.BooleanField(default=False)
    Tue = models.BooleanField(default=False)
    Wed = models.BooleanField(default=False)
    Thu = models.BooleanField(default=False)
    Fri = models.BooleanField(default=False)
    Sat = models.BooleanField(default=False)
    Sun = models.BooleanField(default=False)


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


class Menu(models.Model):
    meal_id = models.Autofield(primary_key=True)
    meal = models.CharField(max_length=50, unique=True)
    vegetarian = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return (self.meal)




from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'provider_register.html', {'form': form})