import random
import math


def showdifference(array1, array2):
    for i in range(len(array1)):
        if (array1[i] != array2[i]):
            print(i, end=" ")


def checkdifference(array1, array2):
    sum = 0
    for i in range(len(array1)):
        if (array1[i] != array2[i]):
            sum = sum + 1
    return sum


def transmission(array2, arraysize, distruptiondegree):
    array = array2.copy()
    todistrupt = math.floor(
        arraysize * distruptiondegree)  # policzenie ilosci bitow do zanegowania (rozmiar obrazu * procent zaklocenia)
    bits = []  # tablica przechowujaca wylosowane bity
    for i in range(todistrupt):  # losowanie bitow w danej ilosci
        done = False
        while (not done):
            bit = random.randint(0, arraysize - 1)  # wylosowanie numeru bitu z zakresu (0,ostatni bit obrazu)
            if (bits.count(bit) == 0):  # jezeli dany bit nie zostal wczesniej  wylosowany to:
                bits.append(bit)  # 1. dodajemy go do tablicy wylosowanych bitow
                if array[bit] == 1:  # 2. negujemy bit o tym numerze w obrazie
                    array[bit] = 0;
                else:
                    array[bit] = 1;
                done = True
            else:  # jezeli zostal wczesniej wylosowany to przechodzimy do petli jeszcze raz
                done = False
    return array


def disrupt(signal, degree):
    print("PRZED TRANMISJĄ")
    print(signal)
    print("\nPO TRANSMISJI")
    afterdistruption = transmission(signal, len(signal), int(degree) / 100)
    print(afterdistruption)
    print("\nNUMERY BITOW KTORE SIE ROZNIA")
    showdifference(signal, afterdistruption)
    if (checkdifference(signal, afterdistruption) != 0):
        stosunek = len(signal) / checkdifference(signal, afterdistruption)
        print()
        print(str(100 / stosunek) + "% zmienionych bitów")
    else:
        print(str(0) + "% zmienionych bitow")
