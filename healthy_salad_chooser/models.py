from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ingredient(models.Model):
	name = models.CharField(max_length=50)
	serving_size = models.IntegerField(default=0)
	serving_unit = models.CharField(max_length=10)
	calories = models.IntegerField(default=0)
	weight_in_oz = models.DecimalField(max_digits=10, decimal_places=2)
	nutrient_density = models.DecimalField(max_digits=10, decimal_places=2)

	def __unicode__(self):
		return self.name

class Salad(models.Model):
	name = models.CharField(max_length=200)
	user = models.ForeignKey(User, related_name='salads')

	class Meta:
		unique_together = ('user', 'name')

	def __unicode__(self):
		return self.name

class SaladIngredient(models.Model):
	ingredient = models.ForeignKey(Ingredient)
	salad = models.ForeignKey(Salad)

