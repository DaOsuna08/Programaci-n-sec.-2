Num_1=int(input('ingresa un numero'))
a=Num_1
if a>100:
    print('El numero es mayor que 100')
elif a%3==0 and a%2==0:
    print('el numero es divisible por 6')
elif a%2==0:
    print('El numero es divisible por 2')
elif a%3==0:
    print('El numero es divisible por 3')
elif a<0:
    print('El numero es negativo')
else:
    print('El numero no cumple ninguna condicion especial')