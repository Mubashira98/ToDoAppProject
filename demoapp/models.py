from django.db import models

# Create your models here.
class todo(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.all