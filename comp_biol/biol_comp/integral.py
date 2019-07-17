from math import sqrt, cos, pi
import matplotlib.pyplot as plt

print('Este script calcula a integral de uma dada função f(x).')
#sqrt(1 + (2*cos((pi*x)/10)*(pi/10))**2)

formula= input("Digite a função para o cálculo da integral: ")

def functTrapezio(x):
  return formula

m= int(input("Digite o número de trapezios: "))
a= int(input("Digite o valor inicial: "))
b= int(input("Digite o valor final: "))
#m=10000
#a= 0
#b= 60
h= (b - a)/m
a1= h/2
#print('h= {:.2f}'.format(h))
a2= functTrapezio(a) + functTrapezio(b)
#print('a2= {:.2f}'.format(a2))
h1= a

xL= [a]
soma1= 0
for i in range(1,m):
  h1= i*h
  xL.append(h1)
  #print(h1)
  soma1+= functTrapezio(h1)
#print('Soma= {:.2f}'.format(soma1))
xL.append(b)
#print(xL)
yL= []
for j in xL:
  yL.append(functTrapezio(j))
#print(yL)

Af= a1*(a2 + (2*soma1))
plt.plot(xL, yL)
plt.show()

print('O cálculo da integral é: {:.9f}'.format(Af))

print('Este script calcula a integral da função e^x para o intervalo de 0< x < 1 pelo método de Simpson.')

def functSimpson(x):
  return formula


h= (b - a)/m
a1= h/3
#print('h= {:.2f}'.format(h))
a2= functSimpson(a) + functSimpson(b)
#print('a2= {:.2f}'.format(a2))
h1= a

soma1= 0
soma2= 0
for i in range(1,m):
  if i%2 == 0:
    h1= i*h
    soma1+= functSimpson(h1)
  else:
    h1= i*h
    soma2+= functSimpson(h1)
    
Af= a1*(a2 + (2*soma1) + (4*soma2))
#plt.plot(xL, yL)
#plt.show()

print('O cálculo da integral é: {:.9f}'.format(Af))