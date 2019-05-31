import scrambler
import receiver
import descrambler
import distrupter


class transmitter:
    def __init__(self, signal, algorythm):
        pure_disrupted = distrupter.distruption2(signal) #zaklocenie sygnalu wysylanego bez scramblera
        scrambled = scrambler.scramble(signal, algorythm) #zescramblowanie sygnalu
        scrambled_disrupted = distrupter.distruption(scrambled) #zaklocenie sygnalu wysylanego ze scramblerem
        descrambled = descrambler.descramble(scrambled_disrupted, algorythm) #odsramblowanie sygnalu zakloconego wysylanego ze scramblerem
        receiver.receiver(signal, pure_disrupted, descrambled, algorythm,scrambled, scrambled_disrupted) #przekazanie sygnalow do programu odbiorczego
