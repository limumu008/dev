from django.db import models


from django.db import models
from django.utils import timezone

question1 = "What's your Mom's first name?"
question2 = "Where were you born?"

class Customer(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_firstName = models.CharField(max_length=50, unique=True)
    user_lastName = models.CharField(max_length=50, unique=True)
    user_email = models.CharField(max_length=50, unique=True)
    user_password = models.CharField(max_length=10)
    answer1 = models.Charfield(max_length=50)
    answer2 = models.Charfield(max_length=50)

    def __str__(self):
        return (self.user_lastName)
