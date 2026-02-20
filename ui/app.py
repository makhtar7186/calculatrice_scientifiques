from calculator.sc_calculator import ScientificCalculator
import tkinter as tk
from tkinter import messagebox


class CalculatorApp:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Scientific Calculator")
        self.root.resizable(False, False)

        self.calculator = ScientificCalculator()

        self._create_widgets()

    # ===============================
    # UI SETUP
    # ===============================

    def _create_widgets(self):

        self.entry = tk.Entry(self.root, width=30, font=("Arial", 14), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("Clear", 5, 0), ("Power", 5, 1),
            ("√", 5, 2), ("Log", 5, 3),
            ("Sin", 6, 0), ("Cos", 6, 1), ("Tan", 6, 2),
            ("(", 6, 3), (")", 7, 0), ("Exp", 7, 1), ("Ln", 7, 2), ("Ans", 7, 3)
        ]

        for (text, row, col) in buttons:
            self._create_button(text, row, col)

        # rendre la grille responsive
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def _create_button(self, text, row, col):

        command_map = {
            "=": self._calculate,
            "Clear": self._clear_entry,
            "Power": lambda: self._add_to_entry("**"),
            "√": lambda: self._apply_scientific(self.calculator.square_root),
            "Log": lambda: self._apply_scientific(self.calculator.logarithm),
            "Sin": lambda: self._apply_scientific(self.calculator.sin),
            "Cos": lambda: self._apply_scientific(self.calculator.cos),
            "Tan": lambda: self._apply_scientific(self.calculator.tan),
            "Ans": lambda: self._apply_scientific(self.calculator.ans)
        }

        command = command_map.get(text, lambda: self._add_to_entry(text))

        tk.Button(
            self.root,
            text=text,
            width=8,
            height=2,
            command=command
        ).grid(row=row, column=col, padx=3, pady=3)

    # ===============================
    # CORE METHODS
    # ===============================

    def _add_to_entry(self, value):
        self.entry.insert(tk.END, value)

    def _clear_entry(self):
        self.entry.delete(0, tk.END)

    def _calculate(self):
        expression = self.entry.get()
        try:
            result = self.calculator.evaluate(expression)
            self._update_entry(result)
        except Exception as e:
            self._show_error(e)

    def _apply_scientific(self, operation):
        try:
            value = float(self.entry.get())
            result = operation(value)
            self._update_entry(result)
        except Exception as e:
            self._show_error(e)

    # ===============================
    # UTILITIES
    # ===============================

    def _update_entry(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, value)

    def _show_error(self, error):
        self._clear_entry()
        messagebox.showerror("Error", str(error))

    def run(self):
        self.root.mainloop()

