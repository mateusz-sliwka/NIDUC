import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import datetime
import matplotlib.pyplot as plt
import math
import matplotlib.cm as cm
import sender
import numpy as np
import collections


def stringhistogram(signal):
    print(type(signal))
    b_e = []
    i = 0
    while i < len(signal) - 1:
        y = 1
        while signal[i] == signal[i + 1] and signal[i] == 0:
            i = i + 1
            y += 1
            if i > len(signal) - 2:
                break
        if (y > 1):
            b_e.append(y)
        i += 1
    x = 0
    b_e.sort(reverse=TRUE)
    counter = collections.Counter(b_e)
    return counter


def signalhistogram(signal):
    signal = signal.voltage
    b_e = []
    i = 0
    while i < len(signal) - 1:
        y = 1
        while signal[i] == signal[i + 1] and signal[i] == 'Z':
            i = i + 1
            y += 1
            if i > len(signal) - 2:
                break
        if (y > 1):
            b_e.append(y)
        i += 1
    x = 0
    b_e.sort(reverse=TRUE)
    counter = collections.Counter(b_e)
    return counter

class receiver:
    def __init__(self, puresignal, puresignaldisrupted, descrambled, algorythm, scrambled, scrambleddisrupted, tab1, tab2):
        window2 = tk.Tk()
        window2.title("Odbiorca sygnału")
        window2.geometry("1400x520")
        ramka0 = tk.Frame()
        ramka1 = tk.Frame(ramka0, pady=20)
        ramka2 = tk.Frame(ramka0, pady=20)
        ramka3 = tk.Frame(ramka0, pady=20)
        ramka6 = tk.Frame(ramka0, pady=20)
        ramka8 = tk.Frame(ramka0, pady=20)

        def newprocess():  # zamkniecie okna odbiorczego, utworzenie nowej, czystej instacji programu
            window2.destroy()
            start = sender.sender()

        def savetofile():  # funkcja pozwalajaca zapisac wyniki do pliku
            file1 = open("results/result-" + str(datetime.datetime.now()) + ".txt", "w")
            file1.write("======WYNIK SRAMBLINGU======\n")
            file1.write("NADAWANY SYGNAŁ (" + str(len(puresignal) * len(puresignal)) + "bitow):\n")
            file1.write(str(puresignal))
            file1.write("\n\n\nSYGNAL ZE SCRAMBLINGIEM:\n ")
            for x in range (len(scrambled.signal)):
                file1.write(str(scrambled.signal[x])+",")
            file1.write("\n")
            for x in range (len(scrambled.voltage)):
                file1.write(str(scrambled.voltage[x])+",")
            file1.write("\n\n\nSYGNAL ZE SCRAMBLINGIEM ZAKLOCONY:\n ")
            for x in range(len(scrambleddisrupted.signal)):
                file1.write(str(scrambleddisrupted.signal[x]) + ",")
            file1.write("\n")
            for x in range(len(scrambleddisrupted.voltage)):
                file1.write(str(scrambleddisrupted.voltage[x]) + ",")
            file1.write("\n\n\nODEBRANY ODSCRAMBLOWANY SYGNAL\n")
            for x in range(len(descrambled.signal)):
                file1.write(str(descrambled.signal[x]) + ",")
            file1.write("\n")
            for x in range(len(descrambled.voltage)):
                file1.write(str(descrambled.voltage[x]) + ",")
            file1.write("\n\n\nODEBRANY SYGNAL WYSYLANY BEZ SCRAMBLINGU\n")
            for x in range(len(puresignaldisrupted)):
                file1.write(str(puresignaldisrupted[x]) + ",")
            file1.write("\n\n\nLICZBA NIEZGODNYCH BITOW W SYGNALU BEZ SCRAMLBINGU: " + str(result))
            file1.write("\nPROCENT NIEZGODNYCH BITOW W SYGNALU BEZ SCRAMLBINGU: " + str(result * 100 / len(puresignal)))
            file1.write("\nLICZBA I DLUGOSCI CIAGOW TYCH SAMYCH BITOW W SYGNALE BEZ SCRAMBLINGU: ")
            tab1 = list(stringhistogram(puresignaldisrupted).keys())
            tab2 = list(stringhistogram(puresignaldisrupted).values())
            for x in range (len(tab1)):
                file1.write("("+str(tab1[x])+","+str(tab2[x])+"),")


            file1.write("\n\nPROCENT NIEZGODNYCH BITOW W SYGNALE ZE SCRAMBLINGIEM: " + str(result2))
            file1.write("\nPROCENT NIEZGODNYCH BITOW W SYGNALU ZE SCRAMLBINGIEM: " + str(scramblingresult))
            file1.write("\nLICZBA I DLUGOSCI CIAGOW TYCH SAMYCH BITOW W SYGNALE ZE SCRAMBLINGIEM: ")
            tab1 = list(signalhistogram(descrambled).keys())
            tab2 = list(signalhistogram(descrambled).values())
            for x in range (len(tab1)):
                file1.write("(" + str(tab1[x]) + "," + str(tab2[x]) + "),")


            file1.write("\n\nOBRAZ WYSYLANY ZE SCRAMBLIGNIEM MA TYLE PUNKTOW PROCENTOWYCH MNIEJ ZAKLOCONYCH BITOW: " + str(
                puresignaldisruptedresult-scramblingresult))


        def array_vs_array(array1, array2):  # zestawienie dwoch sygnalow, pokazanie roznic
            array2 = array2.signal
            licznik = 0
            for i in range(len(array1)):
                if (array1[i] != array2[i]):
                    licznik += 1
            return licznik

        def array_vs_array2(array1, array2):  # zestawienie dwoch sygnalow, pokazanie roznic
            licznik = 0
            for i in range(len(array1)):
                if (array1[i] != array2[i]):
                    licznik += 1
            return licznik

        def fill_empty():  # wypelnienie miejsc na obrazy pustymi, domyslnymi sygnalami
            value = []
            for i in range(250 * 250):
                value.append(255)
            plt.imsave('empty_img.png', np.array(value).reshape(250, 250), cmap=cm.gray)
            image = Image.open("empty_img.png").resize((250, 250))
            photo = ImageTk.PhotoImage(image)
            label = Label(ramka1, image=photo, borderwidth=2, relief="groove")
            label.image = photo
            label.grid(column=0, row=1, sticky=tk.N)
            label = Label(ramka2, image=photo, borderwidth=2, relief="groove")
            label.image = photo
            label.grid(column=0, row=1, sticky=tk.N)
            label = Label(ramka3, image=photo, borderwidth=2, relief="groove")
            label.image = photo
            label.grid(column=0, row=1, sticky=tk.N)

        def receive_puresignal(value2):  # wypelnienie miejsca na sygnal wysylany
            value = []
            for i in range(len(value2)):
                value.append(value2[i])

            plt.imsave('imgs/received_puresignal.png',
                       np.array(value).reshape(int(math.sqrt(len(value))), int(math.sqrt(len(value)))), cmap=cm.gray)
            image = Image.open("imgs/received_puresignal.png").resize((250, 250))
            photo = ImageTk.PhotoImage(image)
            label = Label(ramka1, image=photo, borderwidth=2, relief="groove")
            label.image = photo
            label.grid(column=0, row=1, sticky=tk.N)

        def receive_puresignaldisrupted(value):  # wyplenienie miejsca na signal zaklocony niescramblowany
            stringhistogram(value)
            for i in range(len(value)):
                value[i] = int(value[i])


            plt.imsave('imgs/received_withoutscr.png',
                       np.array(value).reshape(int(math.sqrt(len(value))), int(math.sqrt(len(value)))), cmap=cm.gray)
            image = Image.open("imgs/received_withoutscr.png").resize((250, 250))
            photo = ImageTk.PhotoImage(image)
            label2 = Label(ramka2, image=photo, borderwidth=2, relief="groove")
            label2.image = photo
            label2.grid(column=0, row=1, sticky=tk.N)

        def receive_descrambled(value2):  # wypelnienie miejsca na sygnal po descramblingu
            signalhistogram(value2)
            value = value2.signal
            for i in range(len(value)):
                value[i] = int(value[i])

            plt.imsave('imgs/received_withscrl.png',
                       np.array(value).reshape(int(math.sqrt(len(value))), int(math.sqrt(len(value)))), cmap=cm.gray)
            image = Image.open("imgs/received_withscrl.png").resize((250, 250))
            photo = ImageTk.PhotoImage(image)
            label3 = Label(ramka3, image=photo, borderwidth=2, relief="groove")
            label3.image = photo
            label3.grid(column=0, row=1, sticky=tk.N)



        fill_empty()
        receive_puresignal(puresignal)
        receive_puresignaldisrupted(puresignaldisrupted)
        receive_descrambled(descrambled)

        version = tk.Label(ramka0, text="v0.0", fg="grey", anchor="w", width=33)
        version.grid(row=0, column=0, sticky=tk.NW)

        author = tk.Label(ramka0, text="", fg="grey", width=33)
        author.grid(row=0, column=1, sticky=tk.NW)

        author = tk.Label(ramka0, text="Karasek, Kamieniecki, Śliwka", fg="grey", anchor="e", width=32)
        author.grid(row=0, column=4, sticky=tk.NW)

        label1 = tk.Label(ramka1, text="Przesyłany obraz")
        label1.grid(row=0, column=0, sticky=tk.N)
        # obrazek1
        label3 = tk.Label(ramka1, text="Rozmiar obrazka: " + str(int(math.sqrt(len(puresignal)))) + "x" + str(
            int(math.sqrt(len(puresignal)))) + "px")
        label44 = tk.Label(ramka1, text="Sygnal o dlugosci: " + str(len(puresignal)) + "bitow")
        label44.grid(row=3, column=0)
        label3.grid(row=2, column=0)
        ramka1.grid(row=1, column=0, sticky=tk.N)

        label2 = tk.Label(ramka2, text="Odebrany niescramblowany obraz")
        label2.grid(row=0, column=0)
        # obrazek1

        result = array_vs_array2(puresignal, puresignaldisrupted)
        puresignaldisruptedresult = result * 100 / len(puresignal)
        label5 = tk.Label(ramka2, text="Ilość zniekształconych bitów: " + str(result) + "\nStanowią one " + str(
            result * 100 / len(puresignal)) + " % sygnału")
        label5.grid(row=3, column=0)
        ramka2.grid(row=1, column=1, sticky=tk.N)

        label3 = tk.Label(ramka3, text="Odebrany scramblowany obraz")
        label3.grid(row=0, column=0)
        # obrazek1
        result2 = array_vs_array(puresignal, descrambled)
        label9 = tk.Label(ramka3, text="Metoda scramblingu: " + algorythm)
        label9.grid(row=2, column=0)
        scramblingresult = result2 * 100 / len(puresignal)
        label10 = tk.Label(ramka3, text="Ilość zniekształconych bitów: " + str(result2) + "\nStanowią one " + str(
            scramblingresult) + " % sygnału")
        label10.grid(row=3, column=0)
        ramka1.grid(row=1, column=0)
        ramka3.grid(row=1, column=3, sticky=tk.N)
        ramka0.grid(row=0, column=0)

        ramka4 = tk.Frame(pady=20)
        ramka5 = tk.Frame(ramka4)
        button1 = tk.Button(ramka5, text="Zapisz wynik do pliku", height=2, width=20, fg="black",
                            command=lambda: savetofile())
        button1.grid(row=0, column=0, pady=1)
        button2 = tk.Button(ramka5, text="Nadaj nowy sygnał", command=lambda: newprocess())
        button2.grid(row=1, column=0, pady=5)
        label11 = tk.Label(ramka5, text="Scrambling poprawil skutecznosc o " + str(
            round(puresignaldisruptedresult - scramblingresult,3)) + " punktow procentowych.", width=100, font=('Verdana', 15, 'bold'))
        label11.grid(row=0, column=1)
        ramka5.grid(row=0, column=0)
        ramka4.grid(row=1, column=0)
        ramka6.grid(row=1, column=2)
        ramka7 = tk.Frame(ramka6, pady=20)
        ramka7.grid(row=0, column=0)
        tytul1 = tk.Label(ramka7, text="Dlugosc ciagu")
        tytul1.grid(row=0, column=0)
        tytul2 = tk.Label(ramka7, text="Ilosc wystapien")
        tytul2.grid(row=0, column=1)

        tab3 = list(stringhistogram(puresignaldisrupted).keys())
        tab4 = list(stringhistogram(puresignaldisrupted).values())

        if (len(tab3) > 0):
            dlugosc1 = tk.Label(ramka7, text=tab3[0])
            dlugosc1.grid(row=1, column=0)
            ilosc1 = tk.Label(ramka7, text=tab4[0])
            ilosc1.grid(row=1, column=1)
        if (len(tab3) > 1):
            dlugosc2 = tk.Label(ramka7, text=tab3[1])
            dlugosc2.grid(row=2, column=0)
            ilosc2 = tk.Label(ramka7, text=tab4[1])
            ilosc2.grid(row=2, column=1)
        if (len(tab3) > 2):
            dlugosc3 = tk.Label(ramka7, text=tab3[2])
            dlugosc3.grid(row=3, column=0)
            ilosc3 = tk.Label(ramka7, text=tab4[2])
            ilosc3.grid(row=3, column=1)
        if (len(tab3) > 3):
            dlugosc4 = tk.Label(ramka7, text=tab3[3])
            dlugosc4.grid(row=4, column=0)
            ilosc4 = tk.Label(ramka7, text=tab4[3])
            ilosc4.grid(row=4, column=1)
        if (len(tab3) > 4):
            dlugosc5 = tk.Label(ramka7, text=tab3[4])
            dlugosc5.grid(row=5, column=0)
            ilosc5 = tk.Label(ramka7, text=tab4[4])
            ilosc5.grid(row=5, column=1)
        if (len(tab3) > 5):
            dlugosc6 = tk.Label(ramka7, text=tab3[5])
            dlugosc6.grid(row=6, column=0)
            ilosc6 = tk.Label(ramka7, text=tab4[5])
            ilosc6.grid(row=6, column=1)
        if (len(tab3) > 6):
            dlugosc7 = tk.Label(ramka7, text=tab3[6])
            dlugosc7.grid(row=7, column=0)
            ilosc7 = tk.Label(ramka7, text=tab4[6])
            ilosc7.grid(row=7, column=1)
        if (len(tab3) > 7):
            dlugosc8 = tk.Label(ramka7, text=tab3[7])
            dlugosc8.grid(row=8, column=0)
            ilosc8 = tk.Label(ramka7, text=tab4[7])
            ilosc8.grid(row=8, column=1)
        if (len(tab3) > 8):
            dlugosc9 = tk.Label(ramka7, text=tab3[8])
            dlugosc9.grid(row=9, column=0)
            ilosc9 = tk.Label(ramka7, text=tab4[8])
            ilosc9.grid(row=9, column=1)
        if (len(tab3) > 9):
            dlugosc10 = tk.Label(ramka7, text=tab3[9])
            dlugosc10.grid(row=10, column=0)
            ilosc10 = tk.Label(ramka7, text=tab4[9])
            ilosc10.grid(row=10, column=1)
        if (len(tab3) > 10):
            dlugosc11 = tk.Label(ramka7, text=tab3[10])
            dlugosc11.grid(row=11, column=0)
            ilosc11 = tk.Label(ramka7, text=tab4[10])
            ilosc11.grid(row=11, column=1)
        if (len(tab3) > 11):
            dlugosc12 = tk.Label(ramka7, text=tab3[11])
            dlugosc12.grid(row=12, column=0)
            ilosc12 = tk.Label(ramka7, text=tab4[11])
            ilosc12.grid(row=12, column=1)

        ramka8.grid(row=1, column=4)
        ramka9 = tk.Frame(ramka8, pady=20)
        ramka9.grid(row=0, column=0)
        tytul1 = tk.Label(ramka9, text="Dlugosc ciagu")
        tytul1.grid(row=0, column=0)
        tytul2 = tk.Label(ramka9, text="Ilosc wystapien")
        tytul2.grid(row=0, column=1)

        if (len(tab1)>0):
            dlugosc1 = tk.Label(ramka9, text=tab1[0])
            dlugosc1.grid(row=1, column=0)
            ilosc1 = tk.Label(ramka9, text=tab2[0])
            ilosc1.grid(row=1, column=1)
        if (len(tab1)>1):
            dlugosc2 = tk.Label(ramka9, text=tab1[1])
            dlugosc2.grid(row=2, column=0)
            ilosc2 = tk.Label(ramka9, text=tab2[1])
            ilosc2.grid(row=2, column=1)
        if (len(tab1)>2):
            dlugosc3 = tk.Label(ramka9, text=tab1[2])
            dlugosc3.grid(row=3, column=0)
            ilosc3 = tk.Label(ramka9, text=tab2[2])
            ilosc3.grid(row=3, column=1)
        if (len(tab1)>3):
            dlugosc4 = tk.Label(ramka9, text=tab1[3])
            dlugosc4.grid(row=4, column=0)
            ilosc4 = tk.Label(ramka9, text=tab2[3])
            ilosc4.grid(row=4, column=1)
        if (len(tab1)>4):
            dlugosc5 = tk.Label(ramka9, text=tab1[4])
            dlugosc5.grid(row=5, column=0)
            ilosc5 = tk.Label(ramka9, text=tab2[4])
            ilosc5.grid(row=5, column=1)
        if (len(tab1)>5):
            dlugosc6 = tk.Label(ramka9, text=tab1[5])
            dlugosc6.grid(row=6, column=0)
            ilosc6 = tk.Label(ramka9, text=tab2[5])
            ilosc6.grid(row=6, column=1)
        if (len(tab1)>6):
            dlugosc7 = tk.Label(ramka9, text=tab1[6])
            dlugosc7.grid(row=7, column=0)
            ilosc7 = tk.Label(ramka9, text=tab2[6])
            ilosc7.grid(row=7, column=1)
        if (len(tab1)>7):
            dlugosc8 = tk.Label(ramka9, text=tab1[7])
            dlugosc8.grid(row=8, column=0)
            ilosc8 = tk.Label(ramka9, text=tab2[7])
            ilosc8.grid(row=8, column=1)
        if (len(tab1)>8):
            dlugosc9 = tk.Label(ramka9, text=tab1[8])
            dlugosc9.grid(row=9, column=0)
            ilosc9 = tk.Label(ramka9, text=tab2[8])
            ilosc9.grid(row=9, column=1)
        if (len(tab1)>9):
            dlugosc10 = tk.Label(ramka9, text=tab1[9])
            dlugosc10.grid(row=10, column=0)
            ilosc10 = tk.Label(ramka9, text=tab2[9])
            ilosc10.grid(row=10, column=1)
        if (len(tab1)>10):
            dlugosc11 = tk.Label(ramka9, text=tab1[10])
            dlugosc11.grid(row=11, column=0)
            ilosc11 = tk.Label(ramka9, text=tab2[10])
            ilosc11.grid(row=11, column=1)
        if (len(tab1)>11):
            dlugosc12 = tk.Label(ramka9, text=tab1[11])
            dlugosc12.grid(row=12, column=0)
            ilosc12 = tk.Label(ramka9, text=tab2[11])
            ilosc12.grid(row=12, column=1)

        window2.mainloop()
