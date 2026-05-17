from django.db import models

# Create your models here.

class About(models.Model):
    about_heading = models.CharField(max_length=50)
    about_description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.about_heading
    
    class Meta:
        db_table = 'About'
        verbose_name = 'About'
        verbose_name_plural = 'About'
        


class Links(models.Model):
    platform = models.CharField(max_length=50)
    link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.platform
    
    
    class Meta:
        db_table = 'links'
        verbose_name = 'links'
        verbose_name_plural = 'links'