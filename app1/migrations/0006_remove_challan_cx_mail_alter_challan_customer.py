# Generated by Django 4.2.3 on 2023-09-08 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_employeeloan_action_alter_employeeloan_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challan',
            name='cx_mail',
        ),
        migrations.AlterField(
            model_name='challan',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.customer'),
        ),
    ]
