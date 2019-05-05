import random
import math
import Signal

# TODO GOSIA - PRZEROBIC TEN PROSTY ALGORYTM ZAKLOCENIA WSTAWIONY NIZEJ NA TEN BARDZIEJ AMBITNY O KTORYM ROZMAWIALISMY
def distruption(signal2, distruptiondeg):  # metoda zaklocajaca sygnal
    signal = signal2.signal
    print("\n =====ZAKLOCANIE SYGNALU====")
    distruptiondegree = int(distruptiondeg) / 100
    arraysize = len(signal2.signal)
    todistrupt = math.floor(
        arraysize * distruptiondegree)  # policzenie ilosci bitow do zanegowania (rozmiar obrazu * procent zaklocenia)
    bits = []  # tablica przechowujaca wylosowane bity
    for i in range(todistrupt):  # losowanie bitow w danej ilosci
        done = False
        while (not done):
            bit = random.randint(0, arraysize - 1)  # wylosowanie numeru bitu z zakresu (0,ostatni bit obrazu)
            if (bits.count(bit) == 0):  # jezeli dany bit nie zostal wczesniej  wylosowany to:
                bits.append(bit)  # 1. dodajemy go do tablicy wylosowanych bitow
                if signal2.signal[bit] == 1:  # 2. negujemy bit o tym numerze w obrazie
                    signal2.signal[bit] = 0;
                else:
                    signal2.signal[bit] = 1;
                done = True
        else:  # jezeli zostal wczesniej wylosowany to przechodzimy do petli jeszcze raz
            done = False
    print("Sygnal przed zaklocenie:" + str(signal))
    print("Sygnal zaklocany z intensywnoscia:" + distruptiondeg+"%")
    print("Sygnal po zakloceniu:" + str(signal2.signal))
    print("=====================")
    return signal2

def distruption2(signal, distruptiondeg):  # metoda zaklocajaca sygnal

    print("\n =====ZAKLOCANIE SYGNALU====")
    distruptiondegree = int(distruptiondeg) / 100
    arraysize = len(signal)
    result = signal.copy()
    todistrupt = math.floor(
        arraysize * distruptiondegree)  # policzenie ilosci bitow do zanegowania (rozmiar obrazu * procent zaklocenia)
    bits = []  # tablica przechowujaca wylosowane bity
    for i in range(todistrupt):  # losowanie bitow w danej ilosci
        done = False
        while (not done):
            bit = random.randint(0, arraysize - 1)  # wylosowanie numeru bitu z zakresu (0,ostatni bit obrazu)
            if (bits.count(bit) == 0):  # jezeli dany bit nie zostal wczesniej  wylosowany to:
                bits.append(bit)  # 1. dodajemy go do tablicy wylosowanych bitow
                if result[bit] == 1:  # 2. negujemy bit o tym numerze w obrazie
                    result[bit] = 0;
                else:
                    result[bit] = 1;
                done = True
        else:  # jezeli zostal wczesniej wylosowany to przechodzimy do petli jeszcze raz
            done = False
    print("Sygnal przed zaklocenie:" + str(signal))
    print("Sygnal zaklocany z intensywnoscia:" + distruptiondeg+"%")
    print("Sygnal po zakloceniu:" + str(result))
    print("=====================")
    return result
