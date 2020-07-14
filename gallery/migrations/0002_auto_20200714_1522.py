# Generated by Django 2.2 on 2020-07-14 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='作品标题', max_length=50),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.CharField(default='在这里写作品的简介', max_length=100),
        ),
    ]
