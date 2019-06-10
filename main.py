import sender
from transmitter import transmitter
lista=[]
for x in range (200):
    lista.append(1)
    for y in range (7):
        lista.append(0)
print("Sygnal nadawany: ")
print(lista)
transmitter(lista,"B8ZS")