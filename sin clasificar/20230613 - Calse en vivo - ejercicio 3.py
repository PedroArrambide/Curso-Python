suma = 0
while True:
    num =input("ingresea un numero o coloca 'exit'")
    
    if num.lower() == 'exit':
        break
    elif num.isnumeric():
        num = int(num)
        suma +=num
print ("la suma es: ",suma)

