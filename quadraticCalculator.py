# import modules
import sys
import math


# To take coefficient input from the users
a = float(input("Podaj 'a': "))
# Checking if a is equle zero
if a == 0:
    print("Wartosc zmiennej 'a' nie moze byc zerem.")
    print("Uruchom skrypt ponownie podajac wartosc 'a' rozna od zera.")
    # A was zero, exiting the script
    sys.exit()

# Getting other ceofficients from the user
b = float(input("Podaj 'b': "))
c = float(input("Podaj 'c': "))


if a > 0:
    print("Wartosc wspolczynnika 'a' jest wieksza od zera.")
    print("Ramiona funkcji f(x) = %dx**2 + %dx + %d sa zwrocone do gory." %(a,b,c))
else:
    print("Wartosc wspolczynnika 'a' jest mniejsza od zera.")
    print("Ramiona funkcji f(x) = %dx**2 + %dx + %d sa zwrocone w dol." %(a,b,c))

# Calculating delta
delta = (b**2) - (4*a*c)
print('Delata jest rowna: %d' % delta)

# Check how many solutions we have
if delta == 0:
    # We have only one solution
    x = -b / 2*a
    print("f(x) = %dx**2 + %dx + %d posiada jedeno miejsce zerowe x = %d" %(a,b,c,x))
elif delta > 0:
    # We have two solutions
    x1 = (-b - math.sqrt(delta)) / (2*a)
    x2 = (-b + math.sqrt(delta)) / (2*a)
    print("f(x) = %dx**2 + %dx + %d posiada dwa miejsca zerowe x1 = %d i x2 = %d" %(a,b,c,x1,x2))
else:
    # There is no solution
    print("f(x) = %dx**2 + %dx + %d nie posiada rozwiazan." %(a,b,c))

# End of script
sys.exit()
