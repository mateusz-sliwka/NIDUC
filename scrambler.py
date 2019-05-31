# TODO TRISTAN - ALGORYTH SCRAMBLINGU
from Signal import Signal


def scramble(signal, algorythm):
    scrambledsignal = Signal(signal)
    print("\n =====SCRAMBLOWANIE SYGNALU====")
    print("Sygnal przed scramblingiem:" + ''.join(str(item) for item in signal))
    print (scrambledsignal.voltage)
    print("Sygnal scramblowany algorytmem:"+algorythm)
    print(scrambledsignal.voltage)
    if algorythm == "B8ZS":
        i = 0
        while i< (len(scrambledsignal.signal)-7):
            if zeros(scrambledsignal,i,8):
                        scrambledsignal.voltage[i + 3] = 'V'
                        scrambledsignal.voltage[i + 4] = 'B'
                        scrambledsignal.voltage[i + 6] = 'B'
                        scrambledsignal.voltage[i + 7] = 'V'
            i += 8
    elif algorythm=="HDB3":
        i = 0
        j = 0
        while i< (len(scrambledsignal.signal)-3):
            if scrambledsignal.signal[i] == '1':
                j+=1
            if zeros(scrambledsignal,i,4):
                if (scrambledsignal.voltage[i-1] == 'H' or scrambledsignal.voltage[i-1] == 'L') and j%2 == 0:
                    scrambledsignal.voltage[i] = 'B'
                    scrambledsignal.voltage[i+3] = 'V'
                    j = 0
                elif (scrambledsignal.voltage[i-1] == 'H' or scrambledsignal.voltage[i-1] == 'L') and j%2 == 1:
                    scrambledsignal.voltage[i+3] = 'V'
                    j = 0
            i+=4
    else:
        print("todo")
        #tutaj kod dla AES
    print("Sygnal po scramblingu:"+ ''.join(str(item) for item in scrambledsignal.signal))
    print (scrambledsignal.voltage)
    print("=====================")
    return scrambledsignal
def zeros(scrambledsignal,i,how_many):
    for item in scrambledsignal.signal[i:i+(how_many-1)]:
        if item == 1:
            return False
    return True
