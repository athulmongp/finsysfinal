# Generated by Django 4.2.3 on 2023-09-11 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_remove_challan_cx_mail_alter_challan_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='baldue',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(default='Draft', max_length=150),
        ),
    ]
