import scrambler
import descrambler
import distrupter
import receiver
class transmitter:
    def __init__(self, signal, algorythm):
        pure_disrupted = distrupter.distruption2(signal,algorythm) #zaklocenie sygnalu wysylanego bez scramblera
        scrambled = scrambler.scramble(signal, algorythm) #zescramblowanie sygnalu
        tab1 = list(receiver.signalhistogram(scrambled).keys())
        tab2 = list(receiver.signalhistogram(scrambled).values())
        scrambled_disrupted = distrupter.distruption(scrambled,algorythm) #zaklocenie sygnalu wysylanego ze scramblerem
        descrambled = descrambler.descramble(scrambled_disrupted, algorythm) #odsramblowanie sygnalu zakloconego wysylanego ze scramblerem
        receiver.receiver(signal, pure_disrupted, descrambled, algorythm,scrambled, scrambled_disrupted,tab1,tab2) #przekazanie sygnalow do programu odbiorczego
