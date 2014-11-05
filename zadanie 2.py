# -*- coding: cp1250 -*-

# Zadanie 2
##Funkcja sprawdzaj�ca, czy wyraz jest palindromem

def palindromy(wyraz):
    d = len(wyraz)
    wyraz = (wyraz.replace(" ", "")).lower()
    
    for i in range(d/2):
        if wyraz[i] != wyraz[-1-i]:
            return False
    return True


wyraz = "Ikar rapa� raki"


if palindromy(wyraz) == True:
    print "To zdanie jest palindromem!",
else:
    print "To jest zwyk�e zdanie.",
    
print wyraz, palindromy(wyraz)

