# Generated by Django 2.2.6 on 2019-10-28 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.IntegerField()),
                ('date_created', models.DateTimeField()),
                ('adult', models.IntegerField()),
                ('kids', models.IntegerField()),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'View Customer Bookings',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(help_text='Enter name of the City', max_length=20)),
                ('description', models.TextField(help_text='Describe Your city')),
                ('country', models.CharField(help_text='Enter Country', max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='destination_images')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'view city ',
            },
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(help_text='Enter Community Name', max_length=20)),
                ('region', models.CharField(help_text='Enter Reqion', max_length=20)),
                ('description', models.CharField(help_text='Give Community Description', max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='destination_images')),
                ('duration', models.IntegerField(help_text='Number Of Days/Weeks')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'View Community',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'View Messages',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(default='title', help_text='Enter name of the package', max_length=20)),
                ('description', models.TextField(help_text='Describe Your Package')),
                ('destination', models.CharField(help_text='Enter Location', max_length=500)),
                ('country', models.CharField(help_text='Enter Country', max_length=500)),
                ('duration', models.IntegerField(help_text='Number Of Days')),
                ('Price', models.FloatField(help_text='Enter the Amount')),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=20, null=True)),
                ('image', models.ImageField(blank=True, upload_to='destination_images')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title of your article', max_length=20, unique=True)),
                ('slug', models.SlugField(help_text='Enter type of the article', max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(help_text='Enter the full description of your article here.')),
                ('image', models.ImageField(blank=True, upload_to='destination_images')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('poststatus', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Add & Delete News Articles',
                'ordering': ['-created_on'],
            },
        ),
    ]
