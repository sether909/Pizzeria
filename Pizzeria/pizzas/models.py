from django.db import models
from django_resized import ResizedImageField

# Create your models here.
class Pizza(models.Model):
  pizza_name = models.CharField(max_length=255)
  image = ResizedImageField(default='fallback_image.jpg', upload_to='pizza_images/', blank=True)

class Topping(models.Model):
  pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, null=True)
  topping_name = models.CharField(max_length=255)

class Comment(models.Model):
  pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  comment_text = models.TextField()