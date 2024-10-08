# Generated by Django 5.1 on 2024-08-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelcountry',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time when the {object_name} was created.', null=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='modelstate',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time when the {object_name} was created.', null=True, verbose_name='Created At'),
        ),
    ]
