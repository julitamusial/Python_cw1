from math import sqrt

#-*- coding: utf-8 -*-

#Funkcja kwadratowa, kt�ra liczy wartosc funkcji dla zadanych parametr�w
def funkcja_kwadratowa(a,b,c,x):
    y = a*x**2 + b*x + c
    return y
    

#Funkcja, kt�ra liczy miejsca zerowe tr�jmianu kwadratowego
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

print "Funkcja kwadratowa ma posta�: y = %s*x^2 + %s*x + %s" % (a,b,c)
print "\nDla zadanych parametr�w: a = %s, b = %s, c = %s, \nmiejsca zerowe funkcji kwadratowej wynosz�: " %(a,b,c), miejsca_zerowe(a,b,c)


#Obliczenie warto�ci funkcji w przedziale (-10,10)
dziedzina = range(-10,11)
print "\nWarto�ci funkcji kwadratowej dla argument�w w przedziale (-10,10) wynosz�: "
for i in dziedzina:
    print funkcja_kwadratowa(a,b,c,i),
