import math
import random


def distruption(signal, algorythm):  # metoda zaklocajaca sygnal
    print("\n =====ZAKLOCANIE SCRAMBLOWANEGO SYGNALU====")

    # Początkowe prawdopodobienstwo p
    p = 0.0414
    distruptedsignal = signal
    # Lista ktora bedzie zawierac indeksy poczatku oraz konca ciagu tych samych znakow
    b_e = []
    # Lista ktora bedzie zawierac losowo miejsca zaklocen sygnalu
    n_b = []
    i = 0
    while i < len(distruptedsignal.signal) - 1:
        b_e.append(i)
        while distruptedsignal.voltage[i] == distruptedsignal.voltage[i + 1] and distruptedsignal.voltage[i] == 'Z':
            i += 1
            if i >= len(distruptedsignal.signal) - 1:
                break
        b_e.append(i)

        stala = 3  # zmienna mowiaca o tym jak dlugi ma byc ciag tych samych zankow zeby wystapilo zaklocenie
        if (algorythm == "B8ZS"):
            stala = 4
        # Zaklocanie odbywa sie jezeli pojawi sie ciag powyzej 4 takich samych znakow

        ilosc = b_e[1] - b_e[0] + 1  # ilosc bitow takkich samych w danym ciagu np dla 1111 ilosc =4

        if ilosc >= stala:  # jezeli ilosc jest wieksza niz stala do zaklocenia

            j = 0
            while j <= ilosc - stala:  # iterujemy po roznicy ilosci i stalej
                j += 1
            p = p + j * 0.000012
            p = math.ceil(p * ilosc)
            j = 0
            while j < p:
                n_b.append(random.randint(b_e[0], b_e[
                    1]))
                j += 1
            for j in range(len(
                    n_b)):
                if distruptedsignal.signal[n_b[j]] == 1:
                    distruptedsignal.signal[n_b[j]] = 0
                    distruptedsignal.voltage[n_b[j]] = 'Z'
                elif distruptedsignal.voltage[j - 1] == 'H' and distruptedsignal.signal == 0:
                    distruptedsignal.signal[n_b[j]] = 1
                    distruptedsignal.voltage[n_b[j]] = 'L'
                elif distruptedsignal.signal[n_b[j]] == 0:
                    distruptedsignal.signal[n_b[j]] = 1
                    distruptedsignal.voltage[n_b[j]] = 'H'
        b_e.clear()
        n_b.clear()
        p = 0.0414
        i += 1
    print("Sygnal po zakloceniu:" + ''.join(str(item) for item in distruptedsignal.signal))
    print(distruptedsignal.voltage)
    print("=====================")
    return distruptedsignal


def distruption2(signal, algorythm):  # metoda zaklocajaca sygnal
    # Początkowe prawdopodobienstwo p
    p = 0.0414
    distruptedsignal = []
    for item in signal:
        distruptedsignal.append(item)
    # Lista ktora bedzie zawierac indeksy poczatku oraz konca ciagu tych samych znakow
    b_e = []
    # Lista ktora bedzie zawierac losowo miejsca zaklocen sygnalu
    n_b = []
    i = 0
    while i < len(distruptedsignal) - 1:
        b_e.append(i)
        while distruptedsignal[i] == distruptedsignal[i + 1] and distruptedsignal[i] == 0:
            i += 1
            if i >= len(distruptedsignal) - 1:
                break
        b_e.append(i)
        stala = 3
        if (algorythm == "B8ZS"):
            stala = 4
        ilosc = b_e[1] - b_e[0] + 1
        # Zaklocanie odbywa sie jezeli pojawi sie ciag powyzej 3 takich samych znakow
        if ilosc >= stala:
            j = 0
            while j <= ilosc - stala:
                j += 1
            p = p + j * 0.000012
            p = math.ceil(p * ilosc)
            j = 0
            while j < p:
                n_b.append(random.randint(b_e[0], b_e[1]))
                j += 1
            for j in range(len(n_b)):
                if distruptedsignal[n_b[j]] == 1:
                    distruptedsignal[n_b[j]] = 0
                else:
                    distruptedsignal[n_b[j]] = 1
        b_e.clear()
        n_b.clear()
        p = 0.0414
        i += 1
    print("\n =====ZAKLOCANIE NIESCRAMBLOWANEGO SYGNALU====")
    print("Sygnal po zakloceniU:" + ''.join(str(item) for item in distruptedsignal))
    print("=====================")
    return distruptedsignal
