from view import Display_tk
from model import Decoder
import tkinter as tk


class Controller:

    def __init__(self):
        self.Display = Display_tk()
        self.Decoder = Decoder()
        self.but1 = tk.Button()

    def run(self):
        self.but_tk()
        self.Display.print_info()

    def but_tk(self):
        self.but1 = tk.Button(self.Display.tk,text="Convert", bg="black", fg="white",
                  font=("arial", 15, "bold"), relief=tk.RAISED, padx=20, bd=3,
                              command=self.start_convert,activebackground="red")
        self.but1.place(rely=0.6, relx=0.6)

    def start_convert(self):
        file_adr, first_id, second_id = self.Display.get_values_entr_adres()
        try:
            self.Decoder.csv_convert_to_json(file_adr+".csv", int(first_id), int(second_id))
        except ValueError:
            print("????")
































