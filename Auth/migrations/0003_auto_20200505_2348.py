# Generated by Django 3.0.5 on 2020-05-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_auto_20200504_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]