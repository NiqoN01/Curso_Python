##### Funciones  ##################
def suma12():
    """
    FUNCION QUE NO RECIBE NADA Y NO DEVUELVE NADA
    SOLO GENERA UN MENSAJE

    Returns
    -------
    None.

    """
    print("Mensaje generado en una funcion")
    return
########################### EJERCICIO 1 ##############################
def rest1(num1,num2,num3):
    """
    Funcion que define parametros, pero no devuelve datos
    """
    resta=num1-num2-num3
    print(f"El resultado de restar num1 num2 y num3 es: {resta}")
    return

########################### EJERCICIO 2 ##############################
def data1():
    """
    #Funcion no recibe nada(datos) y si entrega algo
    """
    var1={"A":78,56:1982,"Key3":"Valores"}
   
    return var1

########################### EJERCICIO 3 ##############################
def func1(var1=1,var2=1):
    """
   #Funcion que recibe datos y si entrega algo
    """
    if var1 <= var2:
        print("Multiplicacion")
        return var1*var2
    else:
        print("Division")
        return var1/var2
    
##################################################################
# print("Llamando a la func1")
# func1()
# data1()
# suma12()
    
##################################################################

def funcionv(*var10):
    print(var10)
    return

def prom1(*val2):
    return round(sum(val2)/len(val2),1)