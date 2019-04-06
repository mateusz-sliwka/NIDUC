import random
import math


def printarray(array):
    for j in array:
        print(array[j], end=" ")

def showdifference(array1, array2):
    for i in range(len(array1)):
        if (array1[i] != array2[i]):
            print(i, end=" ")

def checkdifference(array1, array2):
    sum=0
    for i in range(len(array1)):
        if (array1[i] != array2[i]):
            sum=sum+1
    return sum

def transmission(array2, arraysize, distruptiondegree):
    array = array2[:]
    todistrupt = math.floor(
        arraysize * distruptiondegree)  # policzenie ilosci bitow do zanegowania (rozmiar obrazu * procent zaklocenia)
    bits = []  # tablica przechowujaca wylosowane bity
    for i in range(todistrupt):  # losowanie bitow w danej ilosci
        done = False
        while (not done):
            bit = random.randint(0, arraysize - 1)  # wylosowanie numeru bitu z zakresu (0,ostatni bit obrazu)
            if (bits.count(bit) == 0):  # jezeli dany bit nie zostal wczesniej  wylosowany to:
                done = True
                bits.append(bit)  # 1. dodajemy go do tablicy wylosowanych bitow
                if array[bit] == 1:  # 2. negujemy bit o tym numerze w obrazie
                    array[bit] = 0;
                else:
                    array[bit] = 1;
            else:  # jezeli zostal wczesniej wylosowany to przechodzimy do petli jeszcze raz
                done = False
    return array

# OBSZAR TESTOWY
image = []
imagesize = 100
for j in range(imagesize):  # wygenerowanie testowego obrazu o rozmiarze 100 w postaci 010101....
    if j % 2 == 0:
        image.append(0)
    else:
        image.append(1)
distruptionDegree = 0, 2
print("PRZED TRANMISJĄ")
printarray(image)
print("\nPO TRANSMISJI")
afterdistruption = transmission(image, len(image), 0.2)
printarray(afterdistruption)
print("\nNUMERY BITOW KTORE SIE ROZNIA")
showdifference(image, afterdistruption)
stosunek = imagesize/checkdifference(image,afterdistruption)
print()
print(100/stosunek,end=" ")
print("PROCENT ZMIENIONYCH BITÓW")
