import random

import scrambler
import descrambler
import distrupter
import AES2
import receiver


class transmitter:
    def __init__(self, signal, algorythm,now):
        if(algorythm=="AES"):
            napis=""
            for x in range(len(signal)):
                napis+=str(signal[x])
                if (signal[x]==0):
                    napis+="0"
            print(napis)
            print(type(napis))
            key = random.randint(0x00, 0xFF)
            cipher = AES2.AES(key)
            print(type(napis))
            encrypted = cipher.encrypt(napis)
            decrypted = cipher.decrypt(encrypted)
            print(decrypted)

        else:
            pure_disrupted = distrupter.distruption2(signal, algorythm)  # zaklocenie sygnalu wysylanego bez scramblera
            scrambled = scrambler.scramble(signal, algorythm)  # zescramblowanie sygnalu
            tab1 = list(receiver.signalhistogram(scrambled).keys())
            tab2 = list(receiver.signalhistogram(scrambled).values())
            scrambled_disrupted = distrupter.distruption(scrambled,
                                                         algorythm)  # zaklocenie sygnalu wysylanego ze scramblerem
            descrambled = descrambler.descramble(scrambled_disrupted,
                                                 algorythm)  # odsramblowanie sygnalu zakloconego wysylanego ze scramblerem
            receiver.receiver(signal, pure_disrupted, descrambled, algorythm, scrambled, scrambled_disrupted, tab1,
                              tab2,now)  # przekazanie sygnalow do programu odbiorczego
