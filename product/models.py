from django.db import models

# Create your models here.

class ProductCategory(models.Model):
	name = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)

	# display on admin
	def __str__(self):
		return self.name

class Product(models.Model):
	category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	description = models.TextField(null=True)
	price = models.DecimalField(decimal_places=2, max_digits=19)
	image = models.ImageField(upload_to='product/', null=True, blank=True)

	def __str__(self):
		return self.title