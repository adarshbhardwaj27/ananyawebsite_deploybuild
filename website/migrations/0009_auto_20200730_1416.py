# Generated by Django 3.0.8 on 2020-07-30 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20200730_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.AddField(
            model_name='contact',
            name='mess_no',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
