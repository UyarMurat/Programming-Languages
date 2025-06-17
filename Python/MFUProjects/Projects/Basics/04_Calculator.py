# Taschenrechner mit tkinter
import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        # Fenster initialisieren
        self.root = root
        self.root.title("Mathematical Calculator")

        # Eingabefeld erstellen
        self.entry = tk.Entry(root, width=15, borderwidth=3, font=('Arial', 16))
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Letztes Ergebnis speichern für "Ans"
        self.last_result = None

        # Buttons definieren (Layout)
        buttons = [
            ('log', 2, 0), ('√', 2, 1), ('x²', 2, 2), ('x³', 2, 3), ('log₁₀', 2, 4),
            ('(', 3, 0), (')', 3, 1), ('sin', 3, 2), ('cos', 3, 3), ('tan', 3, 4),
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('DEL', 4, 3), ('AC', 4, 4),
            ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('*', 5, 3), ('/', 5, 4),
            ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('+', 6, 3), ('−', 6, 4),
            ('0', 7, 0), (',', 7, 1), ('x10^x', 7, 2), ('Ans', 7, 3), ('=', 7, 4)
        ]

        # Buttons erstellen und an on_click anbinden
        for (text, row, col, colspan) in [(*btn, 1) if len(btn) == 3 else btn for btn in buttons]:
            tk.Button(
                root, text=text, width=5, height=2, font=('Arial', 14),
                command=lambda txt=text: self.on_click(txt)
            ).grid(row=row, column=col, columnspan=colspan)

    def on_click(self, char):
        # Standardzeichen direkt ins Eingabefeld
        if char in '0123456789.+-*/(),':
            self.entry.insert(tk.END, char)

        elif char == 'AC':
            self.entry.delete(0, tk.END)

        elif char == 'DEL':
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current[:-1])

        elif char == 'Ans':
            if self.last_result is not None:
                self.entry.insert(tk.END, str(self.last_result))

        elif char == '=':
            self.evaluate()

        elif char in ['cos', 'sin', '√', 'x10^x']:
            self.handle_math_function(char)

        else:
            # Unbekannte Taste → einfach anhängen
            self.entry.insert(tk.END, char)

    def evaluate(self):
        """Berechnet den aktuellen Ausdruck im Eingabefeld"""
        try:
            result = eval(self.entry.get())
            self.last_result = result
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def handle_math_function(self, func):
        """Führt einfache mathematische Funktionen aus"""
        try:
            x = float(self.entry.get())
            result = None

            if func == 'cos':
                result = math.cos(math.radians(x))
            elif func == 'sin':
                result = math.sin(math.radians(x))
            elif func == '√':
                result = math.sqrt(x)
            elif func == 'x10^x':
                result = 10 ** x

            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))

        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")


# Hauptprogramm starten
root = tk.Tk()
calc = Calculator(root)
root.mainloop()