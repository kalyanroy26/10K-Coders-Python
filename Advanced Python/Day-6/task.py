import requests

data = requests.get("http://fakestoreapi.com/products")

print(data.status_code)
products = data.json()

# print(products)
status = 0


# posting products
for product in products:
    add = requests.post("http://localhost:3000/products",json=product)
    status = add.status_code
print(status)