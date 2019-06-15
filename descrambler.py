# TODO TRISTAN - FUNKCJA DESCRAMBLINGU
from Signal import Signal


def descramble(signal, algorythm):
    print("\n =====DESCRAMBLOWANIE SYGNALU====")
    descrambledsignal = signal
    if algorythm == "B8ZS":
        i = 0
        while i < (len(descrambledsignal.signal) - 4):
            if descrambledsignal.voltage[i] == 'V':
                descrambledsignal.voltage[i] = 'Z'
                descrambledsignal.voltage[i + 1] = 'Z'
                descrambledsignal.voltage[i + 3] = 'Z'
                descrambledsignal.voltage[i + 4] = 'Z'
            i += 1
    else:
        i = 0
        j = 0
        while i < (len(descrambledsignal.signal) - 3):
            if descrambledsignal.signal[i] == '1':
                j += 1
                if j % 2 == 0 and descrambledsignal.voltage[i] == 'B':
                    descrambledsignal.voltage[i] = 'Z'
                    descrambledsignal.voltage[i + 3] = 'Z'
                    j = 0
                elif j % 2 == 1 and descrambledsignal.voltage[i] == 'V':
                    descrambledsignal.voltage[i + 3] = 'Z'
                    j = 0
            i += 1

    for i in range(len(descrambledsignal.signal)):
        if descrambledsignal.voltage[i] == 'H' or descrambledsignal.voltage[i] == 'L':
            descrambledsignal.signal[i] = 1
        else:
            descrambledsignal.signal[i] = 0
    print("Sygnal po descramblingu:" + ''.join(str(item) for item in descrambledsignal.signal))
    print(descrambledsignal.voltage)
    print("=====================")
    return descrambledsignal
