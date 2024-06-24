import numpy as np
import scipy.linalg as sc

z1=complex(input('Ingresa el primer numero complejo='))
print('z1=',z1)
z2=complex(input('Ingresa el segundo numero complejo='))
print('z2=',z2)
print('z1 entre z2=',z1/z2)

A=np.array([[z2.real,-z2.imag],[z2.imag,z2.real]])
print(A)
b=np.array([z1.real,z1.imag])
print(b)
sol=sc.solve(A,b)
print(sol)