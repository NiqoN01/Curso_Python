#REPASO ESTRUCTURA WHILE
#############    1     ####################
# var1 = 0
# while var1 <= 10:
#     print(var1)
#     var1 +=1 # lo mismo que var1 = var1 + 1
################   2   #############################
# dato = "si"  # o con esto  str(input("Desea continuar, ingrese si o no: ")).lower()
# while dato == "si":
#     dato = str(input("Desea continuar, ingrese si o no: ")).lower()
    
    ################   3   #############################
# num = 0
# mult = 0
# while num <= 12:
#     num = num + 1
#     mult = num * 7
#     print(num,"*7: ", mult)
   
  
    ################   4   #############################
# num1=7
# while num1 <=70:
#     print(num1)
#     num1=num1+7

  ################   5   #############################
# dato1 = ""
# while dato1.lower() != "si":
#     dato1 = input("¿Desea continuar con la mutiplicacion? ")
#     if dato1.lower() == "si":
#         # Se ejecuta si la respuesta es "si"
#         print("Continuando...")
      
#         for i in range(1, 10):
#             resultado = 7 * i
#             print("7 x", i, "=", resultado)
#     else:
#         # Se ejecuta si la respuesta no es "si"
#         print("Respuesta incorrecta. Inténtelo de nuevo.")


  ################   6   #############################
# var1 = True
# opc1 = 0
# opc2 = 0
# opc3 = 0
# print("Menu:\n\t1.Mostrar el mensaje de saludo y salir. \n\t2. Volver a mostrar el menu. \n\t3 Salir")
# while var1 == True:
#     opc = input("Ingrese su opcion del menu: ")
#    if opc == 1:
#         print("Saludo")
#         opc = input("Ingrese su opcion del menu: ")
#    elif opc ==2:
#         print("Menu:\n\t1.Mostrar el mensaje de saludo y salir. \n\t2. Volver a mostrar el menu. \n\t3")
#         opc = input("Ingrese su opcion del menu: ")
#    elif opc == 3:
#         print("Saliendo")
        
        
################   Solucion Inge   #############################
var1 = True
while var1 == True:
    print("Menu:\n\t1.Mostrar el mensaje de saludo y salir. \n\t2. Volver a mostrar el menu. \n\t3 Salir")
    var2 = int(input("Ingrese su opcion: "))
    if var2 == 1:
        print("Saludoos")
        var1 = False
    elif var2 == 2:
        var1 = True
    elif var2 == 3:
        print("Programa terminado")
        var1 = False
        