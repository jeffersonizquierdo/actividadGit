def salario():

    sueldo = float (input("Por favor ingrese su sueldo: "))
    horas = float (input("Por favor ingrese la cantidad de horas trabajadas: "))

    hora = 2000

    valorhoras = horas * hora

    if horas > 160:
        nuevosueldo = sueldo - (sueldo * 0.1)
        sueldoneto = nuevosueldo + valorhoras
        print()
        print ('Su total a pagar es de:', sueldoneto)
        print()
    else:
        nuevosueldo = sueldo - (sueldo * 0.07)
        sueldoneto = nuevosueldo + valorhoras
        print()
        print ('Su total a pagar es de:', sueldoneto)
        print()
salario()