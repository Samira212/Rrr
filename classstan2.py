products={"apple":50, "banana": 20, "cherry": 10}
user=input("soz jaz: ")
if user in products:
    print(f"{user}: {products[user]} som")
else:
    print("ERROR")
