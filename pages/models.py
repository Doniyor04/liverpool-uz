from django.db import models

# Create your models here.

# Stadium models
class Stadium(models.Model):
    name = models.CharField(max_length=200, verbose_name="Stadium name")
    established_year = models.PositiveIntegerField(verbose_name="Year established")
    address = models.CharField(max_length=100, verbose_name="Address")
    capacity = models.PositiveIntegerField(verbose_name="Capacity")
    description = models.TextField(verbose_name="About the stadium", blank=True)
    
    def __str__(self):
        return self.name

class StadiumImage(models.Model):
    stadium = models.ForeignKey(
        Stadium, 
        on_delete=models.CASCADE, 
        related_name='images',
        verbose_name="Stadium"
    )
    image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name="Image")
    title = models.CharField(max_length=100, blank=True, verbose_name="Image title")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded at")
    is_main = models.BooleanField(default=False, verbose_name="Main image")
    
    def __str__(self):
        return f"{self.stadium.name} - {self.title or 'Image'}"

# History models
class ClubAchievement(models.Model):
    title = models.CharField(max_length=200, verbose_name="Yutuq nomi")
    numb_achievement = models.PositiveIntegerField(verbose_name="Yutuqlar soni")

class ImportantDate(models.Model):
    title = models.CharField(max_length=200, verbose_name="Date title")
    content = models.TextField(verbose_name="Date content")
    year = models.PositiveIntegerField(verbose_name="Sanasi")
    image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name="Image")

class Legend(models.Model):
    name = models.CharField(max_length=100, verbose_name="Legend name")
    about = models.TextField(verbose_name="About of legend")
    image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name="Legend image")
