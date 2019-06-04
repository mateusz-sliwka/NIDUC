import scrambler
import receiver
import descrambler
import distrupter
import copy


class transmitter:
    def __init__(self, signal, algorythm):
        kopia_si = copy.deepcopy(signal)
        pure_disrupted = distrupter.distruption2(signal) #zaklocenie sygnalu wysylanego bez scramblera
        kopia_pd = copy.deepcopy(pure_disrupted)
        scrambled = scrambler.scramble(signal, algorythm) #zescramblowanie sygnalu
        kopia_scrambled = copy.deepcopy(scrambled)
        scrambled_disrupted = distrupter.distruption(scrambled) #zaklocenie sygnalu wysylanego ze scramblerem
        kopia_sd = copy.deepcopy(scrambled_disrupted)
        descrambled = descrambler.descramble(scrambled_disrupted, algorythm) #odsramblowanie sygnalu zakloconego wysylanego ze scramblerem
        copy_ds = copy.deepcopy(descrambled)
        receiver.receiver(kopia_si, kopia_pd, copy_ds, algorythm,kopia_scrambled, kopia_sd) #przekazanie sygnalow do programu odbiorczego
