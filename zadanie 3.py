from math import sqrt

#Funkcja kwadratowa, która liczy wartoć funkcji dla zadanych parametrów
def funkcja_kwadratowa(a,b,c,x):
    y = a*x**2 + b*x + c
  #  print "Wartosć funkcji wynosi: %f" % y
    return y
    
print "Wartosc funkcji wynosi:"
print funkcja_kwadratowa(1,2,3,5)


#Funkcja, która liczy miejsca zerowe trójmianu kwadratowego
def miejsca_zerowe(a,b,c):

    delta = b**2 - 4 * a * c
    
    if delta > 0:
        x1 = (-b-sqrt(delta)) / 2*a
    	x2 = (-b+sqrt(delta)) / 2*a				
    #	print "Miejsca zerowe to x1 = %f , x2 = %f" % ( x1,x2)	
        return x1, x2
    elif delta == 0:
    	x0 = (b-sqrt(delta)) / 2*a
    #	print "Funkcja posiada tylko jedno miejsce zerowe x0 = %f" % x0
        
    else:
    #	print "Delta ujemna, brak miejsc zerowych"
        return "de;lta"

print miejsca_zerowe(1,3,2)


#Obliczenie wartosci funkcji w przedziale (-10,10)
dziedzina = range(-10,11)

print "Wartosci funkcji dla argumentow w przedziale (-10,10)"
for i in dziedzina:
    print funkcja_kwadratowa(1,2,3,i)
