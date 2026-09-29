import requests

url = requests.get("https://dummyjson.com/recipe")
mydata = url.json()


print(mydata)

print(mydata.keys())