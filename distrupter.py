
import math
import random
from Signal import Signal

def distruption(signal):  # metoda zaklocajaca sygnal
    #Początkowe prawdopodobienstwo p
    p = 0.0414
    distruptedsignal = Signal(signal)
    #Lista ktora bedzie zawierac indeksy poczatku oraz konca ciagu tych samych znakow
    b_e = []
    #Lista ktora bedzie zawierac losowo miejsca zaklocen sygnalu
    n_b = []
    i = 0
    while i < len(distruptedsignal.signal)- 1:
        b_e.append(i)
        while distruptedsignal.signal[i] == distruptedsignal.signal[i+1]:
            i += 1
            if i > len(distruptedsignal.signal) - 2:
                break
        b_e.append(i)
        #Zaklocanie odbywa sie jezeli pojawi sie ciag powyzej 4 takich samych znakow
        if b_e[1] - b_e[0] >= 4:
            j = 0
            while j <= b_e[1] - b_e[0] - 4:
                j+=1
            p = p + j * 0.000012
            p = math.ceil(p*(b_e[1]-b_e[0]))
            j = 0
            while j < p:
                n_b.append(random.randint(b_e[0],b_e[1]))
                j+=1
            for j in range(len(n_b)):
                if distruptedsignal.signal[n_b[j]] == '1':
                    distruptedsignal.signal[n_b[j]] == '0'
                    distruptedsignal.voltage[n_b[j]] == 'Z'
                else:
                    distruptedsignal.signal[n_b[j]] == '1'
                    distruptedsignal.voltage[n_b[j]] == 'H'
        i+=1
    print("\n =====ZAKLOCANIE SYGNALU====")
    print("Sygnal przed zakoceniem:" + signal)
    print("Sygnal po zaklocenie:" + ''.join(str(item) for item in distruptedsignal.signal))
    print("=====================")
    return distruptedsignal


def distruption2(signal):  # metoda zaklocajaca sygnal
    # Początkowe prawdopodobienstwo p
    p = 0.0414
    distruptedsignal = signal
    # Lista ktora bedzie zawierac indeksy poczatku oraz konca ciagu tych samych znakow
    b_e = []
    # Lista ktora bedzie zawierac losowo miejsca zaklocen sygnalu
    n_b = []
    i = 0
    while i < len(distruptedsignal)- 1:
        b_e.append(i)
        while distruptedsignal[i] == distruptedsignal[i+1]:
                i += 1
                if i > len(distruptedsignal) - 2:
                    break
        b_e.append(i)
        # Zaklocanie odbywa sie jezeli pojawi sie ciag powyzej 4 takich samych znakow
        if (b_e[1]-b_e[0]+1) >= 4:
            j = 0
            while j < (b_e[1]-b_e[0]+1) - 4:
                j += 1
            p = p + j * 0.000012
            p = math.ceil(p * (b_e[1] - b_e[0]))
            j = 0
            while j < p:
                n_b.append(random.randint(b_e[0], b_e[1]))
                j+=1
            for j in range(len(n_b)):
                if distruptedsignal[n_b[j]] == '1':
                    distruptedsignal[n_b[j]] == '0'

                else:
                    distruptedsignal[n_b[j]] == '1'
        i += 1
    print("\n =====ZAKLOCANIE SYGNALU====")
    print("Sygnal przed zakoceniem:" + signal)
    print("Sygnal po zaklocenie:" + distruptedsignal)
    print("=====================")
    return distruptedsignal
