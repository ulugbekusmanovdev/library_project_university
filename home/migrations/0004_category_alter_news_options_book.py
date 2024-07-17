# Generated by Django 4.2.4 on 2023-09-21 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_structure_d_img_alter_structure_e_res_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Категория',
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-id',), 'verbose_name': 'Новости', 'verbose_name_plural': 'Новости'},
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('slug', models.SlugField(max_length=100, verbose_name='слаг')),
                ('author', models.CharField(max_length=100, verbose_name='автор')),
                ('year', models.CharField(max_length=100, verbose_name='год')),
                ('pdf', models.FileField(upload_to='book/pdfs/')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='book/photos/')),
                ('recommended_books', models.BooleanField(default=False, verbose_name='рекомендовано')),
                ('top_books', models.BooleanField(default=False, verbose_name='топ')),
                ('business_books', models.BooleanField(default=False, verbose_name='бизнес')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
            options={
                'verbose_name': 'Книги',
                'verbose_name_plural': 'Книги',
                'ordering': ['-id'],
            },
        ),
    ]
