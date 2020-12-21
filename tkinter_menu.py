from tkinter import *
from planet import Planet
import ursina.color as col
from main import Main

class GUI_Startup(Tk):
    def __init__(self, planetlist):
        Tk.__init__(self)

        self.title("Main Menu")

        rahmen1 = Frame(self, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()

        farbe = "#878787"

        abstand_x = 3
        abstand_y = 3

        groesse = 20

        self.bu1 = Button(rahmen1, text="Own config", width=groesse, command=self.no_planets)
        self.bu1.grid(row=1, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu2 = Button(rahmen1, text="2 Planets", width=groesse, command=self.two_planets)
        self.bu2.grid(row=2, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu3 = Button(rahmen1, text="viel", width=groesse, command=self.solar_sys)
        self.bu3.grid(row=3, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        if planetlist:
            self.planet_list = planetlist
        else:
            self.planet_list = []

    def no_planets(self):
        pass

    def two_planets(self):
        planet = Planet(planet_col=col.orange, planet_name="planet1", planet_diameter=1,
                        planet_speed=[10308.531985820431, 27640.154010970804, -0.7364511260199437],
                        coord_x=140699825958.8049,
                        coord_y=-54738590238.00282,
                        coord_z=2510791.537005455)  # create a planet
        self.planet_list.append(planet)

        planet2 = Planet(planet_col=col.red, planet_name='planet2', planet_diameter=1,
                         coord_x=140699825958.8049, coord_y=-54738590238.00282, coord_z=2510791.537005455)
        planet2.set_coords(x=140699825958.8049,
                           y=-54738590238.00282,
                           z=2510791.537005455)
        # self.planet_list.append(planet2)

        start = Main(self.planet_list)

        self.quit()

    def solar_sys(self):
        pass


class GUI_add_Planet(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title("Add Planet")

        rahmen1 = Frame(self, relief=SUNKEN, borderwidth=2)
        rahmen1.pack()

        farbe = "#878787"

        abstand_x = 3
        abstand_y = 3

        groesse = 24

        self.la1_text = StringVar()
        self.la1_text.set("Name:")
        self.la1 = Label(rahmen1, textvariable=self.la1_text, width=groesse, bg=farbe, justify=CENTER)
        self.la1.grid(row=0, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.en1_text = StringVar()
        self.en1_text.set("")
        self.en1 = Entry(rahmen1, width=groesse+9, textvariable=self.en1_text)
        self.en1.grid(row=0, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la2_text = StringVar()
        self.la2_text.set("Mass in kg:")
        self.la2 = Label(rahmen1, textvariable=self.la2_text, width=groesse, bg=farbe, justify=CENTER)
        self.la2.grid(row=1, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.en2_text = StringVar()
        self.en2_text.set("")
        self.en2 = Entry(rahmen1, width=groesse+9, textvariable=self.en2_text)
        self.en2.grid(row=1, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la3_text = StringVar()
        self.la3_text.set("Speed in m/s:")
        self.la3 = Label(rahmen1, textvariable=self.la3_text, width=groesse, bg=farbe, justify=CENTER)
        self.la3.grid(row=2, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.en3_text = StringVar()
        self.en3_text.set("")
        self.en3 = Entry(rahmen1, width=groesse+9, textvariable=self.en3_text)
        self.en3.grid(row=2, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.la4_text = StringVar()
        self.la4_text.set("Position (x;y;z):")
        self.la4 = Label(rahmen1, textvariable=self.la4_text, width=groesse, bg=farbe, justify=CENTER)
        self.la4.grid(row=3, column=0, sticky=E, padx=abstand_x, pady=abstand_y)

        self.en4_1_text = StringVar()
        self.en4_1_text.set("")
        self.en4_1 = Entry(rahmen1, width=round(groesse/3), textvariable=self.en4_1_text)
        self.en4_1.grid(row=3, column=1, sticky=W, padx=abstand_x, pady=abstand_y)

        self.en4_2_text = StringVar()
        self.en4_2_text.set("")
        self.en4_2 = Entry(rahmen1, width=round(groesse/3), textvariable=self.en4_2_text)
        self.en4_2.grid(row=3, column=1, padx=abstand_x, pady=abstand_y)

        self.en4_3_text = StringVar()
        self.en4_3_text.set("")
        self.en4_3 = Entry(rahmen1, width=round(groesse/3), textvariable=self.en4_3_text)
        self.en4_3.grid(row=3, column=1, sticky=E, padx=abstand_x, pady=abstand_y)

        self.bu1 = Button(rahmen1, text="Submit", width=groesse+3, command=self.submit)
        self.bu1.grid(row=4, column=1, padx=abstand_x, pady=abstand_y)

        #self.la4_text = StringVar()
        #self.la4_text.set("Position (x;y;z):")
        #self.la4 = Label(rahmen1, textvariable=self.la2_text, width=groesse, bg=farbe, justify=CENTER)
        #self.la4.grid(row=3, column=0, columnspan=2, padx=abstand_x, pady=abstand_y)

        self.planet_list = []

    def submit(self):
        while 1:
            if self.en1_text and self.en2_text and self.en3_text and self.en4_1_text and self.en4_2_text and self.en4_3_text:
                self.destroy()
                return self.en1_text, self.en2_text, self.en3_text, self.en4_1_text, self.en4_2_text, self.en4_3_text
            else:
                print(HELLO)




if __name__ == '__main__':
    gui = GUI_add_Planet()
    mainloop()