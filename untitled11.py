#REPASO IF ELIF ELSE
ed1 = int(input("Ingrese su edad: "))
if ed1<10:
    print("La edad corresponde a la niñez")
elif ed1>=10 and ed1<18:
    print("La edad correspnde a la adolescencia")
elif ed1>=18 and ed1<30:
    print("La edad corresponde a un adulto joven")
else:
    print("La edad corresponde a la adultez")
    1