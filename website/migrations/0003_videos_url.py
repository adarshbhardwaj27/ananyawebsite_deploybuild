# Generated by Django 3.0.8 on 2020-07-28 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200727_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='url',
            field=models.CharField(default='https://www.youtube.com/channel/UC0Ld6EqhdyQ3xiEtg1fKQXg?view_as=subscriber', max_length=100),
        ),
    ]