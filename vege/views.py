from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def recipes(request):
    if request.method == "POST":
        value = request.POST
        recipe_name = value.get('recipe_name')
        recipe_description = value.get('recipe_description')
        recipe_image = request.FILES['recipe_image']

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
        )
        return redirect('/recipes/')

    queryset = Recipe.objects.all()
    context = {'recipes': queryset}

    return render(request, 'recipes.html', context)


def details(request):
    queryset = Recipe.objects.all()
    context = {'recipes': queryset}
    return render(request, 'dashboard.html', context)


def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/')


def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    value = request.POST

    if request.method == "POST":
        recipe_name = value.get('recipe_name')
        recipe_description = value.get('recipe_description')
        recipe_image = request.FILES['recipe_image']

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image
            queryset.save()
            return redirect('/')
    context = {'recipes': queryset}
    return render(request, 'update_recipe.html', context)
