import time

ue = ["Ireland", "Estonia", "Denmark", "Italy", "Slovenia"]

print(ue[3:3])   # nie wypisze nic, wypisze tylko []
print(ue[-2])    # wypisze przedostatni element - "Italy"
#print(ue[-6])    # błąd, nie posiadamy -6 elementu, licząc od końca "Ireland" przyjmuje numer -5
print(ue[0:5])   # wypisze wszystkie elementy
print(ue[0:3], ue[3:5]) # wywołując komendę ue[0:3] zostanie wypisane "Ireland", "Estonia", "Denmark"
                        # wywołując komendę ue[3:5] zostanie wypisane "Italy", "Slovenia"
print(ue[3:-1])   # wypisze "Italy"
print(ue[-2:-4])  # wypisze []
print(ue[-4:-2])  # wypisze "Estonia", "Denmark"

time.sleep(60)