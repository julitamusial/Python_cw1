##Zadanie 1
##Fizz Buzz

def fizz_buzz(n):
    dane = range (1,n)
    for i in dane:
        if i%3 == 0:
            print "Fizz",
        elif i%5 == 0:
            print "Buzz",
        elif i%3 == 0 and i%5 == 0:         #or i%15 == 0
            print "Fizz Buzz",
        else:
            print i,
    return

fizz_buzz(40)
