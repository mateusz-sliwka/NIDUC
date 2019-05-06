import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import datetime
import matplotlib.pyplot as plt
import math
import matplotlib.cm as cm
import sender
import numpy as np


class receiver:
    def __init__(self, puresignal, puresignaldisrupted, descrambled, algorythm, scrambled, scrambleddisrupted):
        window2 = tk.Tk()
        window2.title("Odbiorca sygnału")
        window2.geometry("900x520")
        ramka0 = tk.Frame()
        ramka1 = tk.Frame(ramka0, pady=20)
        ramka2 = tk.Frame(ramka0, pady=20)
        ramka3 = tk.Frame(ramka0, pady=20)

        def newprocess(): #zamkniecie okna odbiorczego, utworzenie nowej, czystej instacji programu
            window2.destroy()
            start = sender.sender()

        def savetofile(): #funkcja pozwalajaca zapisac wyniki do pliku
            file1 = open("results/result-" + str(datetime.datetime.now()) + ".txt", "w")
            file1.write("======WYNIK SRAMBLINGU======\n")
            file1.write("NADAWANY SYGNAŁ (" + str(len(puresignal) * len(puresignal)) + "bitow):\n")
            file1.write(str(puresignal))
            file1.write("\n\n\nSYGNAL ZE SCRAMBLINGIEM:\n ")
            file1.write(str(scrambled))
            file1.write("\n\n\nSYGNAL ZE SCRAMBLINGIEM ZAKLOCONY:\n ")
            file1.write(str(scrambleddisrupted))
            file1.write("\n\n\nODEBRANY ODSCRAMBLOWANY SYGNAL\n")
            file1.write(str(descrambled))
            file1.write("\n\n\nODEBRANY SYGNAL WYSYLANY BEZ SCRAMBLINGU\n")
            file1.write(str(puresignaldisrupted))
            file1.write("\n\n\nLICZBA NIEZGODNYCH BITOW W SYGNALU BEZ SCRAMLBINGU: " + str(result))
            file1.write("\nPROCENT NIEZGODNYCH BITOW W SYGNALU BEZ SCRAMLBINGU: " + str(result * 100 / len(puresignal)))
            file1.write("\nPROCENT NIEZGODNYCH BITOW W SYGNALE ZE SCRAMBLINGIEM: " + str(result2))
            file1.write("\nPROCENT NIEZGODNYCH BITOW W SYGNALU ZE SCRAMLBINGIEM: " + str(scramblingresult))
            file1.write("\nOBRAZ WYSYLANY ZE SCRAMBLIGNIEM MA TYLE PUNKTO PROCENTOWYCH MNIEJ ZAKLOCONYCH BITOW: " + str(
                scramblingresult - puresignaldisruptedresult))

        def array_vs_array(array1, array2): #zestawienie dwoch sygnalow, pokazanie roznic
            array2=array2.signal
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

        def fill_empty(): #wypelnienie miejsc na obrazy pustymi, domyslnymi sygnalami
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

        def receive_puresignal(value): #wypelnienie miejsca na sygnal wysylany
            plt.imsave('imgs/received_puresignal.png',
                       np.array(value).reshape(int(math.sqrt(len(value))), int(math.sqrt(len(value)))), cmap=cm.gray)
            image = Image.open("imgs/received_puresignal.png").resize((250, 250))
            photo = ImageTk.PhotoImage(image)
            label = Label(ramka1, image=photo, borderwidth=2, relief="groove")
            label.image = photo
            label.grid(column=0, row=1, sticky=tk.N)

        def receive_puresignaldisrupted(value): #wyplenienie miejsca na signal zaklocony niescramblowany
            plt.imsave('imgs/received_withoutscr.png',
                       np.array(value).reshape(int(math.sqrt(len(value))), int(math.sqrt(len(value)))), cmap=cm.gray)
            image = Image.open("imgs/received_withoutscr.png").resize((250, 250))
            photo = ImageTk.PhotoImage(image)
            label2 = Label(ramka2, image=photo, borderwidth=2, relief="groove")
            label2.image = photo
            label2.grid(column=0, row=1, sticky=tk.N)

        def receive_descrambled(value): #wypelnienie miejsca na sygnal po descramblingu
            value = value.signal
            plt.imsave('imgs/received_withscrl',
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
        author.grid(row=0, column=2, sticky=tk.NW)

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
        ramka3.grid(row=1, column=2, sticky=tk.N)
        ramka0.grid(row=0, column=0)

        ramka4 = tk.Frame(pady=20)
        ramka5 = tk.Frame(ramka4)
        button1 = tk.Button(ramka5, text="Zapisz wynik do pliku", height=2, width=20, fg="black",
                            command=lambda: savetofile())
        button1.grid(row=0, column=0, pady=1)
        button2 = tk.Button(ramka5, text="Nadaj nowy sygnał", command=lambda: newprocess())
        button2.grid(row=1, column=0, pady=5)
        label11 = tk.Label(ramka5, text="Scrambling poprawil skutecznosc o " + str(
            scramblingresult - puresignaldisruptedresult) + "%", width=60, font=('Verdana', 15, 'bold'))
        label11.grid(row=0, column=1)
        ramka5.grid(row=0, column=0)
        ramka4.grid(row=1, column=0)

        window2.mainloop()
