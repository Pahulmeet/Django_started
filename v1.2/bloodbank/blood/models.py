from django.db import models
from django.core.urlresolvers import reverse


class Blood_request(models.Model):
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    #state = models.CharField(max_length=250)
    pin_code = models.IntegerField(max_length=10)
    contact1 = models.IntegerField(max_length=10)
    contact2 = models.IntegerField(max_length=10)
    date = models.DateField()
    blood_group = models.CharField(max_length=3)

    def get_absolute_url(self):
        return reverse('blood:index', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name + ' = ' + self.blood_group + ' = ' +self.date.strftime('%Y-%m-%d')

'''
class SignupDonor(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    #password  = models.CharField(widgets=forms.PasswordInput)
    #repassword  = models.CharField(widgets=forms.PasswordInput)
    city = models.CharField(max_length=250)
    pin_code = models.IntegerField(max_length=10)
    state = models.CharField(max_length=250)
    contact1 = models.IntegerField(max_length=10)
    contact2 = models.IntegerField(max_length=10)
    blood_group = models.CharField(max_length=3)

    def get_absolute_url(self):
        return reverse('blood:index', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name + ' = ' + self.blood_group
'''