from django.shortcuts import render
import requests

def index(request):

    url = requests.get("https://dummyjson.com/recipes")
    tags = requests.get("https://dummyjson.com/recipes/tags").json()
    response = url.json()
    context = {

        "data":response["recipes"],
        "tags":tags
    }
    return render(request,"index.html",context)

def search(request):
    query = request.POST.get("query")
    response = requests.get(f"https://dummyjson.com/recipes/search?q={query}").json()
    context = {
        "data" :response["recipes"]
    }
    return render(request,"index.html",context)

def databytags(request,tag):
    print(tag)
    response = requests.get(f"https://dummyjson.com/recipes/tag/{tag}").json()
    tagurl = requests.get("https://dummyjson.com/recipes/tags").json()
    context = {
        "data": response["recipes"],
        "tag": tagurl
    }
    return render(request,"index.html",context)
def mealtype(request,meal):
    response = requests.get(f"https://dummyjson.com/recipes/meal-type/{meal}").json()
    tagurl = requests.get("https://dummyjson.com/recipes/tags").json()
    context = {
        "data": response["recipes"],
        "tag": tagurl
    }
    return render(request, "index.html", context)

def singledata(request,id):
    response = requests.get(f"https://dummyjson.com/recipes/{id}").json()
    context = {
        "data":response
    }
    return render(request,"receipes.html",context)