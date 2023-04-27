#REPASO IF
ed1 = int(input("Ingrese su edad: "))
if ed1>=18:
    print("Usted es mayor de edad")
    tit1=input("Tiene titulo de bachiller: ").lowe()
    if tit1 == "si" :
        print("Si puede sacar la lichencia")
    else:
        print("Usted no tiene titulo de bachiller")
else:
    print("Usted NO es mayor de edad")
    if ed1>=16 and ed1<=18:
        print("Puede obtener un permiso de conduccion")
    else:
        print("No es posible sacar una licencia")