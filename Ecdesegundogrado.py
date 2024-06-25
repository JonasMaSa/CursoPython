import cmath
print("Hola, vamos a calcular la solucion a una ecuacion de segundo grado ax^2+bx+c=0")
a=float(input("Dame el valor de a: "))
print('El coeficiente de x^2 es',a)
b=float(input("Dame el valor de b: "))
print('El coeficiente de x es',b)
c=float(input("Dame el valor de c: "))
print('El termino independiente es',c)

d = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
e = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)   
print('La primer solucion es:', d)
print('La segunda solucion es:', e)

