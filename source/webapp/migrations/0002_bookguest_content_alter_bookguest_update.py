# Generated by Django 4.1.3 on 2022-11-12 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookguest',
            name='content',
            field=models.TextField(default='sadsadasd', max_length=300, verbose_name='Content'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookguest',
            name='update',
            field=models.DateField(auto_now_add=True, verbose_name='Update'),
        ),
    ]
