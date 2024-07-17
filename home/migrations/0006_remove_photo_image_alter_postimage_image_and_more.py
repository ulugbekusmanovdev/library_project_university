# Generated by Django 4.2.4 on 2023-09-27 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_photo_alter_category_options_postimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='image',
        ),
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.photo'),
        ),
    ]
