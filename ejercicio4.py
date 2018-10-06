def esPar(numero):
    if numero%2 != 0:
        return bool(0)
    else:
        return bool(1)


def esMultiplo(num1, num2):
 num3 = num1/num2
 if float(num3).is_integer() == bool(1):
     print(num1,"es múltiplo de", num2)
 else:
    print(num1,"no es múltiplo de", num2)


num = int(input("Introduce un numero a comprobar... el resultado es un booleano :p\n"))
print(esPar(num))
res = int(input("Introduce el primer número\n"))
res2 = int(input("Introduce el segundo número\n"))
esMultiplo(res, res2)

# Sean a y b dos números enteros tales que a != 0. Diremos que "a" divide a "b" o "a" es divisor de "b" si
# existe un número entero q tal que b = a * q.
# Por tanto...
# a divide a b ⇐⇒ b = aq; q ∈Z⇐⇒ b es múltiplo de a
# Podemos, a partir de nuestra premisa, deducir que si b/a = q y q es un número entero.

