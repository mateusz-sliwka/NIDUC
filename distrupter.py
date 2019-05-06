
import math
import random
import Signal

def distruption(signal):  # metoda zaklocajaca sygnal
    #Początkowe prawdopodobienstwo p
    p = 0.0414
    distruptedsignal = signal
    #Lista ktora bedzie zawierac indeksy poczatku oraz konca ciagu tych samych znakow
    b_e = []
    #Lista ktora bedzie zawierac losowo miejsca zaklocen sygnalu
    n_b = []
    for i in range(len(distruptedsignal.signal)-2):
        b_e.append(i)
        juz=True
        while distruptedsignal.signal[i] == distruptedsignal.signal[i+1] and juz!=False:
            if i< len(distruptedsignal.signal) - 1:
                i+=1
            else:
                juz=False
        b_e.append(i)
        #Zaklocanie odbywa sie jezeli pojawi sie ciag powyzej 4 takich samych znakow
        if b_e[1] - b_e[0] >= 4:
            j = 0
            while j <= b_e[1] - b_e[0] - 4:
                j+=1
            p = p + j* 0.000012
            p = math.ceil(p*(b_e[1]-b_e[0]))
            j = 0
            while j < p:
                n_b.append(random.randint(b_e[0],b_e[1]))
            for j in range(len(n_b)):
                if distruptedsignal.signal[n_b[j]] == '1':
                    distruptedsignal.signal[n_b[j]] == '0'
                    distruptedsignal.voltage[n_b[j]] == 'Z'
                else:
                    distruptedsignal.signal[n_b[j]] == '1'
                    distruptedsignal.voltage[n_b[j]] == 'H'
        i+=1
    print("\n =====ZAKLOCANIE SYGNALU====")
    print("Sygnal przed zakoceniem:" + ''.join(str(item) for item in signal.signal))
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
    for i in range(len(distruptedsignal)-2):
        b_e.append(i)

        juz=True
        while distruptedsignal[i] == distruptedsignal[i+1] and juz!=False:

            if (i < len(distruptedsignal) - 3):
                i += 1
            else:
                juz=False
        b_e.append(i)
        # Zaklocanie odbywa sie jezeli pojawi sie ciag powyzej 4 takich samych znakow

        if b_e[1] - b_e[0] >= 4:
            j = 0
            while j <= b_e[1] - b_e[0] - 4:

                j += 1
            p = p + j * 0.000012
            p = math.ceil(p * (b_e[1] - b_e[0]))
            j = 0

            while j < p:
                print("tu sie wyklada")
                n_b.append(random.randint(b_e[0], b_e[1]))
            for j in range(len(n_b)):
                if distruptedsignal[n_b[j]] == '1':
                    distruptedsignal[n_b[j]] == '0'

                else:
                    distruptedsignal[n_b[j]] == '1'

        i += 1
    print("\n =====ZAKLOCANIE SYGNALU====")
    print("Sygnal przed zakoceniem:" + ''.join(str(item) for item in signal))
    print("Sygnal po zaklocenie:" + ''.join(str(item) for item in distruptedsignal))
    print("=====================")
    return distruptedsignal
