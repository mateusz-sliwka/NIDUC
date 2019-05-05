# TODO TRISTAN - ALGORYTH SCRAMBLINGU
from Signal import Signal


def scramble(signal, algorythm):
    print("\n =====SCRAMBLOWANIE SYGNALU====")
    scrambledsignal = Signal(signal)
    if algorythm == "B8ZS":
        i = 0
        while i< (len(scrambledsignal.signal)-7):
            if zeros(scrambledsignal,i,8):
                if i == 0:
                    if scrambledsignal.voltage[i] == 'H':
                        scrambledsignal.signal[i + 3] = '1'
                        scrambledsignal.voltage[i + 3] = 'H'
                        scrambledsignal.signal[i + 4] = '1'
                        scrambledsignal.voltage[i + 4] = 'L'
                        scrambledsignal.signal[i + 6] = '1'
                        scrambledsignal.voltage[i + 6] = 'L'
                        scrambledsignal.signal[i + 7] = '1'
                        scrambledsignal.voltage[i + 7] = 'H'
                    else:
                        scrambledsignal.signal[i + 3] = '1'
                        scrambledsignal.voltage[i + 3] = 'L'
                        scrambledsignal.signal[i + 4] = '1'
                        scrambledsignal.voltage[i + 4] = 'H'
                        scrambledsignal.signal[i + 6] = '1'
                        scrambledsignal.voltage[i + 6] = 'H'
                        scrambledsignal.signal[i + 7] = '1'
                        scrambledsignal.voltage[i + 7] = 'L'
                else:
                    if scrambledsignal.voltage[i - 1] == 'H':
                        scrambledsignal.signal[i + 3] = '1'
                        scrambledsignal.voltage[i + 3] = 'H'
                        scrambledsignal.signal[i + 4] = '1'
                        scrambledsignal.voltage[i + 4] = 'L'
                        scrambledsignal.signal[i + 6] = '1'
                        scrambledsignal.voltage[i + 6] = 'L'
                        scrambledsignal.signal[i + 7] = '1'
                        scrambledsignal.voltage[i + 7] = 'H'
                    else:
                        scrambledsignal.signal[i + 3] = '1'
                        scrambledsignal.voltage[i + 3] = 'L'
                        scrambledsignal.signal[i + 4] = '1'
                        scrambledsignal.voltage[i + 4] = 'H'
                        scrambledsignal.signal[i + 6] = '1'
                        scrambledsignal.voltage[i + 6] = 'H'
                        scrambledsignal.signal[i + 7] = '1'
                        scrambledsignal.voltage[i + 7] = 'L'
            i += 1
    else:
        i = 0
        j = 0
        while i< (len(scrambledsignal.signal)-3):
            if scrambledsignal.signal[i] == '1':
                j+=1
            if zeros(scrambledsignal,i,4):
                if scrambledsignal.voltage[i-1] == 'H' and j%2 == 0:
                    scrambledsignal.signal[i] = '1'
                    scrambledsignal.voltage[i] = 'L'
                    scrambledsignal.signal[i+3] = '1'
                    scrambledsignal.voltage[i+3] = 'L'
                    j = 0
                elif scrambledsignal.voltage[i-1] == 'H' and j%2 == 1:
                    scrambledsignal.signal[i+3] = '1'
                    scrambledsignal.voltage[i+3] = 'H'
                    j = 0
                elif scrambledsignal.voltage[i-1] == 'L' and j%2 == 0:
                    scrambledsignal.signal[i] = '1'
                    scrambledsignal.voltage[i] = 'H'
                    scrambledsignal.signal[i+3] = '1'
                    scrambledsignal.voltage[i+3] = 'H'
                    j = 0
                elif scrambledsignal.voltage[i-1] == 'L' and j%2 == 1:
                    scrambledsignal.signal[i+3] = '1'
                    scrambledsignal.voltage[i+3] = 'L'
                    j = 0

            i+=1
    print("Sygnal przed scramblingiem:" + signal)
    print("Sygnal scramblowany algorytmem:"+algorythm)
    print("Sygnal po scramblingu:"+scrambledsignal.signal)
    print (scrambledsignal.voltage)
    print("=====================")
    return scrambledsignal
def zeros(scrambledsignal,i,how_many):
    for item in scrambledsignal.signal[i:i+(how_many-1)]:
        if item == '1':
            return False
    return True
scramble("1100000000","B8ZS")