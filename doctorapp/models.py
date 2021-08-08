from django.db import models
from django.urls import reverse


# Create your models here.
class department(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=150,unique=True)
    img=models.ImageField(upload_to="depart")


    class Mete:
        ordering=('name',)
        verbose_name="department"
        verbose_name_plural="departments"

    def get_url(self):
            return reverse('departfun', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Doctor(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=150,unique=True)
    qualification=models.CharField(max_length=150)
    desc=models.TextField()
    img=models.ImageField(upload_to='doctor')
    depart = models.ForeignKey(department, on_delete=models.CASCADE)
    available=models.BooleanField()

    class Mete:
        ordering=('name',)
        verbose_name="doctor"
        verbose_name_plural="doctors"

    def get_url(self):
        return reverse('doctfunc', args=[self.depart.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)
