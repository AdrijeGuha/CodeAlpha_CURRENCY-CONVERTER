import customtkinter as ctk
from forex_python.converter import CurrencyRates
import pandas as pd
from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x250")
        self.title("Convert Currency")
        self.iconbitmap("./img/CurrencyExchange.ico")
        ctk.set_appearance_mode("System") 
        ctk.set_default_color_theme("dark-blue") 

        # add widgets to app
        label = ctk.CTkLabel(self, text="Currency Converter", font=("Time New Roman" ,32,"bold"))
        label.place(relx=0.5, rely=0.01, anchor=ctk.N)
        
        # Input TextBox
        self.sorc_txt = ctk.CTkTextbox(self, font=("Roboto" ,14), width=200, height=25, wrap=ctk.WORD, activate_scrollbars=False) 
        self.sorc_txt.insert("0.0", "0.000")
        self.sorc_txt.place(relx=0.4, rely=0.3, anchor=ctk.E)

        # Output TextBox
        self.dest_txt = ctk.CTkTextbox(self, font=("Roboto" ,14), width=200, height=25, wrap=ctk.WORD) 
        self.dest_txt.insert("0.0", "0.000")
        self.dest_txt.place(relx=0.6, rely=0.3, anchor=ctk.W)

        file = pd.read_csv("./currencyDict.csv")
        curr_lst = file["Currency"].to_list()
        self.dist = file.set_index(["Currency"]).T

        # Input currency selection Dropdown
        self.combo_sor = ctk.CTkOptionMenu(self,values=curr_lst, hover=True) 
        self.combo_sor.place(relx=0.4, rely=0.45, anchor=ctk.E) 
        self.combo_sor.set("AUD - Australia Dollar")

        # Conversion Button
        button = ctk.CTkButton(master=self, text="Convert", hover=True, hover_color="green", command=self.convert)
        button.place(relx=0.5, rely=0.7, anchor=ctk.S)

        # Output currency selection Dropdown
        self.combo_dest = ctk.CTkOptionMenu(self,values=curr_lst, hover=True) 
        self.combo_dest.place(relx=0.6, rely=0.45, anchor=ctk.W) 
        self.combo_dest.set("AUD - Australia Dollar")

        # img = ImageTk.PhotoImage(Image.open("./img/swap.png").resize((20, 20), Image.ANTIALIAS))
        img = ctk.CTkImage(Image.open("./img/swap.png").resize((20, 20), Image.LANCZOS))
        # Switching button
        button = ctk.CTkButton(master=self, image=img, text="", hover=True, width=5, height=5, command=self.switch, compound=ctk.TOP)
        button.place(relx=0.5, rely=0.49, anchor=ctk.S)


    def convert(self): # Action function for the convertion button
        from_currency = str(self.dist[self.combo_sor.get()]["Currency Code"])
        to_currency = str(self.dist[self.combo_dest.get()]["Currency Code"])
        amount = float(self.sorc_txt.get(1.0,ctk.END))

        cr = CurrencyRates()
        result = cr.convert(from_currency, to_currency, amount)

        self.dest_txt.delete("0.0",ctk.END) # Delete previous entry of the output box
        self.dest_txt.insert("0.0", f"{result:.3f}") # Insert New Entry in the input box


    def switch(self):
        temp1 = str(self.dist[self.combo_dest.get()].name)
        temp2 = str(self.dist[self.combo_sor.get()].name)
        self.combo_sor.set(temp1)
        self.combo_dest.set(temp2)


if __name__ == "__main__":
    app = App()
    app.mainloop()