# Generated by Django 4.2.3 on 2023-08-28 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_employeeloan'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeloan',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]