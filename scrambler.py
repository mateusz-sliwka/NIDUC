# TODO TRISTAN - ALGORYTH SCRAMBLINGU
from Signal import Signal

def scramble(signal, algorythm):
    scrambledsignal = Signal(signal)
    print("\n =====SCRAMBLOWANIE SYGNALU====")
    print("Sygnal przed scramblingiem:" + ''.join(str(item) for item in signal))
    print (scrambledsignal.voltage)
    print("Sygnal scramblowany algorytmem:"+algorythm)
    if algorythm == "B8ZS":
        i = 0
        while i< (len(scrambledsignal.signal)-7):
            if zeros(scrambledsignal,i,8):
                scrambledsignal.voltage[i + 3] = 'V'
                scrambledsignal.voltage[i + 4] = 'B'
                scrambledsignal.voltage[i + 6] = 'B'
                scrambledsignal.voltage[i + 7] = 'V'
                i += 7
            i += 1
    else:
        i = 0
        j = 0
        while i< (len(scrambledsignal.signal)-3):
            if scrambledsignal.signal[i] == '1':
                j+=1
            if zeros(scrambledsignal,i,4):
                if  j%2 == 0:
                    scrambledsignal.voltage[i] = 'B'
                    scrambledsignal.voltage[i+3] = 'V'
                    j = 0
                    i += 3
                elif j%2 == 1:
                    scrambledsignal.voltage[i+3] = 'V'
                    j = 0
                    i += 3
            i+=1
    print("Sygnal po scramblingu:"+ ''.join(str(item) for item in scrambledsignal.signal))
    print (scrambledsignal.voltage)
    print("=====================")
    return scrambledsignal
def zeros(scrambledsignal,i,how_many):
    for item in scrambledsignal.signal[i:i+how_many]:
        if item == 1:
            return False
    return True
