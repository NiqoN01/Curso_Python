# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 18:06:57 2023

@author: HP
"""

try:
    var1,var2=0,90
    #import nombre1
    print(var2/var1)
except (ZeroDivisionError,TypeError,ModuleNotFoundError):
    print("Ocurre una excepcion, se ejecuta EXCEPT")
else:
    print("Esta ejecutandose el bloque else")
finally:
    print("Esta ejecutandose FINALLY")