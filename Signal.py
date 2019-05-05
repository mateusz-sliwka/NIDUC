class Signal:
    def __init__(self, signal):
        self.signal = list(signal)
        self.voltage = ['Z'] * len(signal)
        i = 0
        while i<len(signal):
            if signal[i] == '1' and i == 0:
                self.voltage[i]='H'
            else:
                if signal[i] == '1' and self.voltage[i-1] == 'H':
                    self.voltage[i] = 'L'
                elif self.signal[i] =='1':
                    self.voltage[i] = 'H'
            i+=1
