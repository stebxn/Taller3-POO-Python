import tkinter as tk
from tkinter import messagebox
import math

class Notas:
    def __init__(self):
        self.listaNotas = [0.0] * 5

    def calcularPromedio(self):
        suma = sum(self.listaNotas)
        return suma / len(self.listaNotas)

    def calcularDesviacion(self):
        prom = self.calcularPromedio()
        suma_cuadrados = sum([(nota - prom) ** 2 for nota in self.listaNotas])
        return math.sqrt(suma_cuadrados / len(self.listaNotas))

    def calcularMenor(self):
        return min(self.listaNotas)

    def calcularMayor(self):
        return max(self.listaNotas)

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.notas = Notas()
        self.inicio()

    def inicio(self):
        self.title("Notas")
        self.geometry("280x380")
        self.resizable(False, False)
        
        self.etiquetas_notas = []
        self.campos_notas = []

        for i in range(5):
            label = tk.Label(self, text=f"Nota {i+1}:")
            label.place(x=20, y=20 + i * 30)
            self.etiquetas_notas.append(label)

            entry = tk.Entry(self)
            entry.place(x=105, y=20 + i * 30, width=135)
            self.campos_notas.append(entry)
        
        self.calcular_btn = tk.Button(self, text="Calcular", command=self.calcular_notas)
        self.calcular_btn.place(x=20, y=170, width=100)

        self.limpiar_btn = tk.Button(self, text="Limpiar", command=self.limpiar_campos)
        self.limpiar_btn.place(x=125, y=170, width=80)
        
        self.promedio_lbl = tk.Label(self, text="Promedio = ")
        self.promedio_lbl.place(x=20, y=210)

        self.desviacion_lbl = tk.Label(self, text="Desviación = ")
        self.desviacion_lbl.place(x=20, y=240)
        
        self.mayor_lbl = tk.Label(self, text="Nota mayor = ")
        self.mayor_lbl.place(x=20, y=270)
        
        self.menor_lbl = tk.Label(self, text="Nota menor = ")
        self.menor_lbl.place(x=20, y=300)
    
    def calcular_notas(self):
        try:
            notas_temporales = []
            for i in range(5):
                nota_texto = self.campos_notas[i].get()
                if not nota_texto:
                    raise ValueError("Todos los campos de nota son obligatorios.")
                
                nota_float = float(nota_texto)
                
                if not (0.0 <= nota_float <= 5.0):
                    raise ValueError(f"La nota '{nota_float}' está fuera del rango válido (0.0 a 5.0).")
                
                notas_temporales.append(nota_float)
            
            self.notas.listaNotas = notas_temporales
            
            promedio = self.notas.calcularPromedio()
            desviacion = self.notas.calcularDesviacion()
            mayor = self.notas.calcularMayor()
            menor = self.notas.calcularMenor()
            
            self.promedio_lbl.config(text=f"Promedio = {promedio:.2f}")
            self.desviacion_lbl.config(text=f"Desviación = {desviacion:.2f}")
            self.mayor_lbl.config(text=f"Nota mayor = {mayor:.2f}")
            self.menor_lbl.config(text=f"Nota menor = {menor:.2f}")

        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e))
            
    def limpiar_campos(self):
        for campo in self.campos_notas:
            campo.delete(0, tk.END)
        
        self.promedio_lbl.config(text="Promedio = ")
        self.desviacion_lbl.config(text="Desviación = ")
        self.mayor_lbl.config(text="Nota mayor = ")
        self.menor_lbl.config(text="Nota menor = ")

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()