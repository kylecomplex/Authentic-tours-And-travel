from django.db import models
from django.utils import timezone
from datetime import datetime

from django.contrib.auth.models import User







class Post(models.Model):
    IS_IT_PUBLISH_OR_DRAFT = (
        (0, 'Draft'),
        (1, 'Publish'),
    )
    title = models.CharField(max_length=20, unique=True,
                             help_text='Enter the title of your article')
    slug = models.SlugField(max_length=200, unique=True,
                            help_text='Enter type of the article')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now_add=True,)
    content = models.TextField(
        help_text='Enter the full description of your article here.')
    image = models.ImageField(upload_to='destination_images', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    poststatus = models.IntegerField(choices=IS_IT_PUBLISH_OR_DRAFT, default=0)

    def __str__(self):
        return '%s' % (self.title)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'Add & Delete News Articles'


class Message(models.Model):

    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.IntegerField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.name, self.subject)

    class Meta:
        verbose_name_plural = 'View Messages'


class Community(models.Model):
    community_name = models.CharField(
        max_length=20, help_text='Enter Community Name')
    region = models.CharField(max_length=20, help_text='Enter Reqion')
    description = models.CharField(
        max_length=20, help_text='Give Community Description')
    image = models.ImageField(upload_to='destination_images', blank=True)
    duration = models.IntegerField(help_text='Number Of Days/Weeks')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.community_name, self.region)

    class Meta:
        verbose_name_plural = 'View Community'


class City(models.Model):

    city_name = models.CharField(
        max_length=20, help_text='Enter name of the City')
    description = models.TextField(help_text='Describe Your city')
    country = models.CharField(max_length=500, help_text='Enter Country')
    image = models.ImageField(upload_to='destination_images', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.city_name, self.country)

    class Meta:
        verbose_name_plural = 'view city '


class Booking(models.Model):

    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()
    date_created = models.DateTimeField()
    adult = models.IntegerField()
    kids = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return '%s %s' % (self.name, self.message)

    class Meta:
        verbose_name_plural = 'View Customer Bookings'


class Package(models.Model):

    package_name = models.CharField(
        max_length=20, help_text='Enter name of the package', default="title")
    description = models.TextField(help_text='Describe Your Package')
    destination = models.CharField(max_length=500, help_text='Enter Location')
    country = models.CharField(max_length=500, help_text='Enter Country')
    duration = models.IntegerField(help_text='Number Of Days')
    Price = models.FloatField(help_text='Enter the Amount')
    discount_price = models.FloatField(blank=True, null=True)
    slug = models.SlugField(max_length=20, null=True)
    image = models.ImageField(upload_to='destination_images', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.package_name )

    @classmethod
    def search_by_name(cls,search_term):
        search = cls.objects.filter(name__icontains=search_term)
        return search