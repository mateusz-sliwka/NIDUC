#Klasa reprezentujaca sygnal w postaci binarnej oraz w postaci napiec
class Signal:
    def __init__(self, signal):
        self.signal = list(signal)
        # Z- Napiece zerowe, H- Napiecie wysokie, L- napiecie niskie
        self.voltage = ['Z'] * len(signal)
        i = 0
        while i<len(self.signal):
            if self.signal[i] == 1 and i == 0:
                self.voltage[i]='H'
            elif self.signal[i] == 1 and self.voltage[i-1] == 'H':
                self.voltage[i] = 'L'
            elif self.signal[i] == 1:
                self.voltage[i] = 'H'
            i+=1
