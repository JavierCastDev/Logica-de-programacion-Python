#¿ES UN NÚMERO PRIMO?

#Escribe un programa que se encargue de comprobar si un número es o no primo.
#Hecho esto, imprime los números primos entre 1 y 100.


def es_primo():
    for i in range(2,100):
        primo = True
        for j in range(2,i):
            if i % j == 0:
                primo = False
                break
        if primo:
            print(f"{i} es primo")

es_primo()