from django.core.validators import RegexValidator, EmailValidator
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    def __iter__(self):
        products = self.products.filter(is_visible=True)
        for product in products:
            yield product

    class Meta:
        ordering = ('sort', 'name')
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='images/products/')
    price = models.DecimalField(max_digits=7, decimal_places=2)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort', 'name')

    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=500)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort', 'name')
        verbose_name_plural = 'Slides'

    def __str__(self):
        return self.name

class About(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort', 'name')
        verbose_name_plural = 'About'

    def __str__(self):
        return self.name

class Offer(models.Model):
    name = models.CharField(max_length=50)
    percent = models.DecimalField(max_digits=2, decimal_places=0)
    status = models.CharField(max_length=3, choices=[('Off', 'Off'), ('On', 'On')], default='Off')
    photo = models.ImageField(upload_to='images/offers/')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort', 'name')

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='images/clients/')
    grade = models.CharField(max_length=7, choices=[('Great', 'Great'), ('Average', 'Average'), ('Bad', 'Bad')], default='Average')

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ('sort', 'name')

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    location = models.TextField(max_length=100)
    number = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    text = models.TextField(max_length=200)
    opening_hours = RichTextField(max_length=500)

    facebook_link = models.URLField()
    twitter_link = models.URLField()
    linkedin_link = models.URLField()
    instagram_link = models.URLField()
    pinterest_link = models.URLField()

class Reservation(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message='Invalid phone number.')

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, validators=[phone_regex])
    email = models.EmailField(max_length=100)
    count = models.PositiveSmallIntegerField(default=1)
    date = models.DateField()

    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.name} - {self.phone} - {self.email}'
