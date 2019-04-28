import math

a = float(input("Podaj 'a': "))
if a == 0:
    raise ValueError("Wartosc zmiennej 'a' nie moze byc zerem.")

b = float(input("Podaj 'b': "))
c = float(input("Podaj 'c': "))

if a > 0:
    print("Wartosc wspolczynnika 'a' jest wieksza od zera.")
    print("Ramiona funkcji f(x) = %dx**2 + %dx + %d sa zwrocone do gory." %(a,b,c))
else:
    print("Wartosc wspolczynnika 'a' jest mniejsza od zera.")
    print("Ramiona funkcji f(x) = %dx**2 + %dx + %d sa zwrocone w dol." %(a,b,c))

delta = (b*b) - (4*a*c)
print('Delata jest rowna: %d' % delta)

if delta == 0:
    x = -b / 2*a
    print("f(x) = %dx**2 + %dx + %d posiada jedeno miejsce zerowe x = %d" %(a,b,c,x))
elif delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print("f(x) = %dx**2 + %dx + %d posiada dwa miejsca zerowe x1 = %d i x2 = %d" %(a,b,c,x1,x2))
else:
    print("f(x) = %dx**2 + %dx + %d nie posiada rozwiazan." %(a,b,c))
