# Generated by Django 3.0.7 on 2020-07-30 12:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=1000)),
                ('video_thumbnail', models.ImageField(default='', upload_to='website/images')),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
                ('url', models.CharField(default='https://www.youtube.com/channel/UC0Ld6EqhdyQ3xiEtg1fKQXg?view_as=subscriber', max_length=100)),
            ],
        ),
    ]