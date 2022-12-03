# Generated by Django 4.0.5 on 2022-07-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0002_subscribe_option_alter_subscribe_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='option',
            field=models.CharField(choices=[('W', 'Weekly'), ('M', 'Monthly')], default='M', max_length=2),
        ),
    ]