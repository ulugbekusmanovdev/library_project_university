# Generated by Django 4.2.4 on 2023-10-11 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_photo_image_alter_postimage_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newspaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Газета',
                'verbose_name_plural': 'Газета',
                'ordering': ('id',),
            },
        ),
    ]
