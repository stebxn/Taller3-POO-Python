import tkinter as tk
from tkinter import messagebox
import math

class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return math.pi * self.altura * (self.radio**2)

    def calcular_superficie(self):
        area_lado_a = 2 * math.pi * self.radio * self.altura
        area_lado_b = 2 * math.pi * (self.radio**2)
        return area_lado_a + area_lado_b

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return (4/3) * math.pi * (self.radio**3)

    def calcular_superficie(self):
        return 4 * math.pi * (self.radio**2)

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()
        
    def calcular_volumen(self):
        return ((self.base**2) * self.altura) / 3

    def calcular_superficie(self):
        area_base = self.base**2
        area_lateral = 2 * self.base * self.apotema
        return area_base + area_lateral

class VentanaCilindro(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cilindro")
        self.geometry("280x210")
        self.resizable(False, False)

        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=100, y=20, width=135)

        tk.Label(self, text="Altura (cms):").place(x=20, y=50)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=100, y=50, width=135)

        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.place(x=100, y=80, width=135)

        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):")
        self.lbl_volumen.place(x=20, y=110)

        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):")
        self.lbl_superficie.place(x=20, y=140)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            altura = float(self.campo_altura.get())
            cilindro = Cilindro(radio, altura)
            self.lbl_volumen.config(text=f"Volumen (cm3): {cilindro.volumen:.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {cilindro.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número.")

class VentanaEsfera(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Esfera")
        self.geometry("280x200")
        self.resizable(False, False)
        
        tk.Label(self, text="Radio (cms):").place(x=20, y=20)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.place(x=100, y=20, width=135)
        
        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.place(x=100, y=50, width=135)
        
        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):")
        self.lbl_volumen.place(x=20, y=90)
        
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):")
        self.lbl_superficie.place(x=20, y=120)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            esfera = Esfera(radio)
            self.lbl_volumen.config(text=f"Volumen (cm3): {esfera.volumen:.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {esfera.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número.")

class VentanaPiramide(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pirámide")
        self.geometry("280x240")
        self.resizable(False, False)

        tk.Label(self, text="Base (cms):").place(x=20, y=20)
        self.campo_base = tk.Entry(self)
        self.campo_base.place(x=120, y=20, width=135)

        tk.Label(self, text="Altura (cms):").place(x=20, y=50)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.place(x=120, y=50, width=135)
        
        tk.Label(self, text="Apotema (cms):").place(x=20, y=80)
        self.campo_apotema = tk.Entry(self)
        self.campo_apotema.place(x=120, y=80, width=135)
        
        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn_calcular.place(x=120, y=110, width=135)
        
        self.lbl_volumen = tk.Label(self, text="Volumen (cm3):")
        self.lbl_volumen.place(x=20, y=140)
        
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2):")
        self.lbl_superficie.place(x=20, y=170)

    def calcular(self):
        try:
            base = float(self.campo_base.get())
            altura = float(self.campo_altura.get())
            apotema = float(self.campo_apotema.get())
            piramide = Piramide(base, altura, apotema)
            self.lbl_volumen.config(text=f"Volumen (cm3): {piramide.volumen:.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {piramide.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número.")

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.geometry("350x160")
        self.resizable(False, False)

        self.btn_cilindro = tk.Button(self, text="Cilindro", command=self.abrir_cilindro)
        self.btn_cilindro.place(x=20, y=50, width=80)

        self.btn_esfera = tk.Button(self, text="Esfera", command=self.abrir_esfera)
        self.btn_esfera.place(x=125, y=50, width=80)

        self.btn_piramide = tk.Button(self, text="Pirámide", command=self.abrir_piramide)
        self.btn_piramide.place(x=225, y=50, width=100)

    def abrir_cilindro(self):
        VentanaCilindro(self)

    def abrir_esfera(self):
        VentanaEsfera(self)

    def abrir_piramide(self):
        VentanaPiramide(self)

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()