import scrambler
import receiver
import descrambler
import distrupter


class transmitter:
    def __init__(self, signal, degree, algorythm):
        pure_disrupted = distrupter.distruption2(signal, degree) #zaklocenie sygnalu wysylanego bez scramblera
        scrambled = scrambler.scramble(signal, algorythm) #zescramblowanie sygnalu
        scrambled_disrupted = distrupter.distruption(scrambled, degree) #zaklocenie sygnalu wysylanego ze scramblerem
        descrambled = descrambler.descramble(scrambled_disrupted, algorythm) #odsramblowanie sygnalu zakloconego wysylanego ze scramblerem
        receiver.receiver(signal, pure_disrupted, descrambled, algorythm, degree, scrambled, scrambled_disrupted) #przekazanie sygnalow do programu odbiorczego
