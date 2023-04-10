# Generated by Django 3.0.8 on 2020-07-30 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mess_no',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(default='', max_length=350),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
    ]