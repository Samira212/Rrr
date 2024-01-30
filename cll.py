products = {"apple": 50, "banana": 20, "cherry": 10}
num = input('soz jaz: ')

if num in products.keys():
    del products[num]
    print(products)
else:
    print("error")