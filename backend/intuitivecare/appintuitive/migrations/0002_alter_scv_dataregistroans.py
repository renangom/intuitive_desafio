# Generated by Django 4.0.1 on 2022-05-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appintuitive', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scv',
            name='DataRegistroANS',
            field=models.DateField(),
        ),
    ]
