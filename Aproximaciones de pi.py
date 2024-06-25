import math
print('Vamos a calcular aproximaciones al valor de pi mediante una serie')
n=int(input(print('Introduce el número de terminos que quieres en tu serie')))
p = 0
if 0 <= n:
  for i in range(n):
    p = p + (4*((-1)**i)/((2*i)+1))
  print('El valor de pi es aproximadamente', p)
  print('El valor exacto de pi es', math.pi)
else:
  print('El número de terminos debe ser mayor o igual a 0')
