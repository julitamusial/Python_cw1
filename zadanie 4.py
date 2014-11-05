# -*- coding: cp1250 -*-

#Zadanie 4
#Usuwanie duplikatów z listy

ZOO = ["pies", "kot", "pies", "lew","krowa","kot", "pingwin"]

def duplikat(lista):
    output = []

    for i in lista:
        if i not in output:
            output.append(i)
    return output

print "Lista pierwotna : " ,ZOO
print "Lista bez duplikatów: ", duplikat(ZOO)


## Druga fukcja, wykorzystująca metodę set()
def dupli(ZOO):
    ZOO = set(ZOO)
    return list(ZOO)

print "Lista bez duplikatów (v2): ", dupli(ZOO);
