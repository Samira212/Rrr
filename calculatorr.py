num1 = int(input("Первое число: "))
num2 = int(input("Второе число: "))
num = input("Выберите операцию: +, -, *, /, %:")
if num == "+":
    print(num1+num2)
elif num == "-":
    print(num1-num2)
elif num == "*":
    print(num1*num2)
elif num == "%":
    print(num1%num2) 
elif num == " ":
    print(num1**num2)
elif num== "/":
    if num2 != 0:
        print(num1/num2)
    else:
        print("Нельзя делить на ноль")
else:
        print("Ошибка")



        
