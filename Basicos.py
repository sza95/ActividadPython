from datetime import date


print("##############Bienvenido!##############\n")


opcion = int(input("##############Ingrese la opción a la que desea entrar##############\n"))
 
if opcion == 1:
    base = int(input("Ingrese la base del triangulo:\n"))
    altura = int(input("Ingrese la altura del triangulo:\n"))

    area = int(base*altura)/2
    print(f"El area del triangulo es : {area}")
if opcion == 2:
    dolar = int(input("Ingrese el los dolares que convertira:\n"))

    pesos_colombianos = dolar*3850
    print(f"El valor de {dolar}$ USD a pesos Colombianos es {pesos_colombianos}")
if opcion == 3:
    celcius = int(input("Ingrese el valor de los grados en celcius:\n"))

    fahrenheit = (celcius*(9/5)+32)

    print(f"{celcius}°C son {fahrenheit}°F")
if opcion == 4:
    lustros = int(input("Ingrese la cantidad de lustros a convertir:\n"))

    segundos = lustros*157680000

    print(f"{lustros} lustros equivalen a {segundos} segundos")
if opcion == 5:
    luz = 299792
    km_marte = 225000000

    segundos = round(km_marte/luz)

    print(f"La luz del sol tarda {round(segundos)} segundos en llegar al planeta Marte")
if opcion == 6:

    CONST_llanta = 50
    circuferencia = 3.1416*CONST_llanta
    
    km = circuferencia/100000

    vueltas = 1/km

    print(f"La llanta da {round(vueltas)} vueltas en 1KM")
if opcion == 7:
    angulo = 35
    sombra = 120/angulo

    print(sombra)

if opcion == 8:
    persona1 = int(input("Ingrese la edad de la persona #1: \n"))
    persona2 = int(input("Ingrese la edad de la persona #2: \n"))

    igual = persona1 == persona2
    print(igual)

if opcion == 9:
    hoy = date.today()
    nacimiento = date(1995,3,15)

    diferencia = (hoy.year-nacimiento.year) * 12 + hoy.month - nacimiento.month
    print(f"Han pasado {diferencia} meses desde {nacimiento} hasta hoy")


if opcion == 10:
    nota1 = int(input("Ingrese la nota para Español:\n"))
    nota2 = int(input("Ingrese la nota para Matemáticas:\n"))
    nota3 = int(input("Ingrese la nota para Economía:\n"))
    nota4 = int(input("Ingrese la nota para Programación:\n"))
    nota5 = int(input("Ingrese la nota para Ingles:\n"))

    suma = (nota1+nota2+nota3+nota4+nota5)

    promedio = suma/5

    print(f"El promedio del estudiante es: {promedio}")