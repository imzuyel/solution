# Generated by Django 2.2 on 2019-04-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190428_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='solution',
            field=models.CharField(default='Solution', max_length=10),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='URI Online Judge | 100', max_length=100),
        ),
    ]