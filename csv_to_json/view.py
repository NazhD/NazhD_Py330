import tkinter as tk


class Display_tk:

    def __init__(self):
        self.tk = tk.Tk()
        self.vol1 = tk.Entry()
        self.vol2 = tk.Entry(width=7)
        self.vol3 = tk.Entry(width=7)
        self.data = 0

    def print_info(self):

        self.tk.geometry("500x200")
        self.tk.title("CSV_CONVERT_TO_JSON")
        self.tk.resizable(False, False)
        label1 = tk.Label(text="Путь к файлу", bg="#504739", fg="white", font=("arial", 15, "bold"), padx=20, bd=3)
        label1.place(rely=0.1, relx=0.1)
        label2 = tk.Label(text="id", bg="#504739", fg="white", font=("arial", 15, "bold"),
                          padx=20, bd=3)
        label2.place(rely=0.32, relx=0.33)
        lable_info = tk.Label(text=".csv", bg="#504739", fg="white", font=("arial", 15, "bold"))
        lable_info.place(rely=0.13, relx=0.75)
        self.tk.config(bg="#504739")
        self.vol1.place(rely=0.15, relx=0.5)
        self.vol2.place(rely=0.35, relx=0.5)
        self.vol3.place(rely=0.35, relx=0.655)
        self.tk.mainloop()

    def get_values_entr_adres(self):
        self.data = self.vol1.get(), self.vol2.get(), self.vol3.get()
        return self.data





















