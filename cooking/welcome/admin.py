from django.contrib import admin
from .models import Ingredient, Recipe
# Register your models here.

# from .models import MyModel

# admin.site.register(MyModel)

admin.site.register(Ingredient)
# admin.site.register(Recipe)

class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['name', 'ingredients__name']

admin.site.register(Recipe, RecipeAdmin)