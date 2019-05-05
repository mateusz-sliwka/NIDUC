import array

class Signal:
    def _init_(self, signal):
        self.signal = signal
        self.voltage = array.array('B', ['Z' * len(signal)])
        i = 0
        while i<len(self.signal):
            if self.voltage[i] == '1' and i == 0:
                self.voltage[i]='H'
            else:
                if self.voltage[i-1] == '1' and self.voltage[i-1] == 'H':
                    self.voltage[i] = 'L'
                elif self.voltage[i-1] =='1':
                    self.voltage[i] = 'H'
        i+=1
