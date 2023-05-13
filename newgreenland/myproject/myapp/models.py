from django.db import models

# Create your models here.
class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    BuyerName = models.CharField(max_length=225)
    Address = models.CharField(max_length=225)
    def __str__(self):
        return self.BuyerName

class Style(models.Model):
    id = models.AutoField(primary_key=True)
    BuyerName = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    StyleCode = models.CharField(max_length=225,unique=True)
    ItemName = models.CharField(max_length=225,blank=True,null=True)
    Buyer = models.CharField(max_length=225)
    def __str__(self):
        return self.StyleCode

class ProductionLine(models.Model):
    id = models.AutoField(primary_key=True)
    ProductionLine = models.CharField(max_length=255)

    def __str__(self):
        return self.ProductionLine