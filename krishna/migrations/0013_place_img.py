# Generated by Django 4.1.1 on 2023-03-02 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishna', '0012_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='img',
            field=models.ImageField(default=1, upload_to='pics'),
        ),
    ]