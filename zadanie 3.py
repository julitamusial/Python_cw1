#Zadanie 3
#Fukcja kwadratowa

from math import sqrt
#-*- coding: utf-8 -*-

#Funkcja kwadratowa, która liczy wartosc funkcji dla zadanych parametrów
def funkcja_kwadratowa(a,b,c,x):
    y = a*x**2 + b*x + c
    return y
    

#Funkcja, która liczy miejsca zerowe trójmianu kwadratowego
def miejsca_zerowe(a,b,c):

    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b-sqrt(delta)) / 2*a
        x2 = (-b+sqrt(delta)) / 2*a				
        return x1, x2
    elif delta == 0:
    	x0 = (b-sqrt(delta)) / 2*a
    else:
        return None
        
a = -2
b = 1
c = 1

print "Funkcja kwadratowa ma postaæ: y = %s*x^2 + %s*x + %s" % (a,b,c)
print "\nDla zadanych parametrów: a = %s, b = %s, c = %s, \nmiejsca zerowe funkcji kwadratowej wynosz¹: " %(a,b,c), miejsca_zerowe(a,b,c)


#Obliczenie wartoœci funkcji w przedziale (-10,10)
dziedzina = range(-10,11)
print "\nWartoœci funkcji kwadratowej dla argumentów w przedziale (-10,10) wynosz¹: "
for i in dziedzina:
    print funkcja_kwadratowa(a,b,c,i),
