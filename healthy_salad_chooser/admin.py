from django.contrib import admin
from healthy_salad_chooser.models import Ingredient, Salad, SaladIngredient

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Salad)
admin.site.register(SaladIngredient)