from django.db import models
from ckeditor.fields import RichTextField

class About(models.Model):
    
    body = RichTextField()

    def __str__(self):
        return str("About")
    

class Design(models.Model):
    body = RichTextField()

    def __str__(self):
        return str("Design")
    

class Development(models.Model):
    body = RichTextField()

    def __str__(self):
        return str("Development")
    

class Database(models.Model):
    body = RichTextField()

    def __str__(self):
        return str("Database")
    
    

class Portfolio(models.Model):
    portfolio_title = models.CharField(max_length=255)
    portfolio_img = models.ImageField(upload_to="portfolios")
    portfolio_url = models.TextField(null=True)

    def __str__(self):
        return str(self.portfolio_title)
    
