año = int(input("Ingrese el año a calcular: "))
if año % 400 == 0:
    print("El año es bisiesto.")
elif año % 100== 0:
    print("El año no es bisiesto.") 
else:
    if año % 4 == 0:
        print("El año es bisiesto.")
    else:
        print("El año no es bisiesto.")