from django.db import models

STATUS_CHOICES = [('Active', 'Активная'), ('Blocked', 'Заблокирован')]


# Create your models here.


class BookGuest(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name='Name')
    email = models.EmailField(max_length=30, null=False, blank=False, verbose_name='Email')
    content = models.TextField(max_length=300, null=False, blank=False, verbose_name='Content')
    create = models.DateField(auto_now_add=True, verbose_name='Create')
    update = models.DateField(auto_now=True, verbose_name='Update')
    choice = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name='Choice')

    def __str__(self):
        return f'{self.pk}.{self.name}'


