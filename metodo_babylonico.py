# -*- coding: utf-8 -*-
"""Metodo Babylonico.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hoHTjlHj5G6LVuPTLKkL4qsICWYxJHUJ
"""

import numpy as np

raiz = float(input("Dame el valor del cual quieres la raíz: "))
aprox = float(input("Da una aproximación: "))


for x in range(10):
    aprox = .5*(aprox + raiz/aprox)

print("La raíz aproximada de {0} es {1}"
         .format(raiz, aprox))

print("La raíz de {0} es {1:50.49} ".format(raiz, np.sqrt(raiz)))

orden = abs(np.sqrt(raiz) - aprox)

print('El error es de {0}'.format(orden))