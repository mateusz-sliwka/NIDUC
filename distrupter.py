from Signal import Signal
import math
import random

# TODO TRISTAN - PRZEROBIC TEN PROSTY ALGORYTM ZAKLOCENIA WSTAWIONY NIZEJ NA TEN BARDZIEJ AMBITNY O KTORYM ROZMAWIALISMY
def distruption(signal):  # metoda zaklocajaca sygnal
    p = 0.0414
    distruptedsignal= Signal(signal)
    b_e = []
    n_b = []
    for i in range(len(distruptedsignal.signal)):
        b_e.append(i)
        while distruptedsignal.signal[i] == distruptedsignal.signal[i+1]:
            if i< len(distruptedsignal.signal) - 1:
                i+=1
            else:
                break
        b_e.append(i)
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
distruption("11111111")
