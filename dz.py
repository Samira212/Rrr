customer={"name": "Azamat", "last": "Kurbanov", "country": "KG", "age": 33}
k=input("Ключ жаз: ")
if k in customer.keys():
    print(customer[k])
else:
    print("Андай ключ жок")