# Generated by Django 4.0.4 on 2022-11-04 20:43

from django.db import migrations, models
import photos.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='author',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=photos.models.get_upload),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]