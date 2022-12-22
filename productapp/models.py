from django.db import models



class ComapanyModel(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(null=True,blank=True)

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=150)
    company = models.ForeignKey(ComapanyModel,on_delete=models.CASCADE,null=True,blank=True,related_name='company_products')
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images',blank=False,null=False)
    def __str__(self):
        return self.name






