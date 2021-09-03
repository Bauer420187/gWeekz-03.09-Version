
# Create your models here.
from django.db import models
from django.db.models.fields import IntegerField, SlugField
from django.utils import translation
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from .validators import file_size



class Game(models.Model):
    different_games = models.CharField(max_length=100)
    image = models.ImageField(null = True,upload_to = "images/games_images/")

    def __str__(self):
        return self.different_games

class Tag(models.Model):
   caption = models.CharField(max_length=30) 

   def __str__(self):
       return self.caption
class Video(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to = "video/%y", validators =[file_size])
    
    def __str__(self):
        return self.caption


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(null = True,max_length=20000)
    image = models.ImageField(null = True , upload_to = "images/product_images/")
    price = models.FloatField()
    games = models.ManyToManyField(Game)
    tags = models.ManyToManyField(Tag)
    slug = SlugField(unique= True)
    max_subscriptions = models.IntegerField(default = 1,
    validators = [
        MaxValueValidator(10000),
        MinValueValidator(1)
    ])
 

    def __str__(self):
        return self.name
    #Render Images mit einer Model Methode um entweder das Image zu rendern oder ein leeren string, damit kein Error Code entsteht 

    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ""
        return url


class Customer(models.Model):
    user = models.OneToOneField(User, null = True, blank = True, on_delete= models.CASCADE)
    description = models.CharField(null = True,max_length=20000)
    email = models.CharField(max_length=200)
    image = models.ImageField(null = True , blank = True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)

    def __str__(self):
     return self.user


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null =True, blank = True)
    date_ordered = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False)
    transaction_id = models.CharField(max_length= 100, null = True)
    
    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete= models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null= True)
    quantity = models.IntegerField(default=0, null = True , blank = True)
    date_added = models.DateTimeField(auto_now_add=True)



class Room(models.Model):
    """Represents chat rooms that users can join"""
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)

    def __str__(self):
        """Returns human-readable representation of the model instance."""
        return self.name

