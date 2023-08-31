import tkinter as tk
from tkinter import scrolledtext

class Lexer:
    def __init__(self):
        self.delimiters = [".", ";"]
        self.keywords = ["public", "static", "void", "main", "int", "for"]
        self.operators = ["=", "+", "-", "*", "/","<"]
        self.numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.apertura = ['(']
        self.cierre = [')']
        self.llaveA = ['{']
        self.llaveB = ['}']
        self.llaveC = ['[']
        self.llaveD = [']']
        self.number_pattern = r'\d+'

    def is_valid_identifier(self, token):
        return token == "n" or (token.isalpha() and token != "main" and token != "int")

    def tokenize(self, text):
        self.tokens = self.delimiters + self.keywords + self.operators + self.numbers + self.apertura + self.cierre + self.llaveA + self.llaveB + self.llaveC + self.llaveD
        arreglo = []
        current_token = ""

        for char in text:
            if char in self.tokens:
                if current_token != "":
                    arreglo.append(current_token)
                current_token = ""

                arreglo.append(char)
            else: 
                if char.isspace():
                    if current_token != "":
                        arreglo.append(current_token)
                    current_token = ""
                else:
                    current_token += char

        if current_token != "":
            arreglo.append(current_token)

        return arreglo

    def analyze(self, text):
        arreglo = self.tokenize(text)
        result = ""

        total_delimitadores = 0
        total_reservadas = 0
        total_numeros = 0
        total_operadores = 0
        total_identificadores = 0
        total_PA = 0
        total_PC = 0
        total_LA = 0
        total_LC = 0
        total_ER = 0
        total_CA = 0
        total_CC = 0

        for token in arreglo:
            if token in self.delimiters:
                result += f"{token} | Delimitador\n" 
                total_delimitadores += 1
            elif token in self.keywords:
                result += f"{token} | Palabra reservada\n"
                total_reservadas += 1
            elif token in self.operators:
                result += f"{token} | Operador\n"
                total_operadores += 1
            elif token in self.numbers:
                result += f"{token} | Número\n"
                total_numeros += 1
            elif self.is_valid_identifier(token):
                result += f"{token} | Identificador\n"
                total_identificadores += 1
            elif token in self.apertura:
                result += f"{token} | Parentecis de apertura\n"
                total_PA += 1
            elif token in self.cierre:
                result += f"{token} | Parentecis de cierre\n"
                total_PC += 1
            elif token in self.llaveA:
                result += f"{token} | Llave de apertura\n"
                total_LA += 1
            elif token in self.llaveB:
                result += f"{token} | Llave de cierre\n"
                total_LC += 1
            elif token in self.llaveC:
                result += f"{token} | Corchete abierto\n"
                total_CA += 1
            elif token in self.llaveD:
                result += f"{token} | Corchete cerrado\n"
                total_CC += 1
            else:
                result += f"{token} | Error lexico x_x\n"
                total_ER += 1

        if text.strip():
            result += f"\nTotal delimitadores: {total_delimitadores}\n"
            result += f"Total reservadas: {total_reservadas}\n"
            result += f"Total numeros: {total_numeros}\n"
            result += f"Total operadores: {total_operadores}\n"
            result += f"Total identificadores: {total_identificadores}\n"
            result += f"Total parentesis abierto: {total_PA}\n"
            result += f"Total parentecis cerrado: {total_PC}\n"
            result += f"Total llaves abiertos: {total_LA}\n"
            result += f"Total llaves cerradas: {total_LC}\n"
            result += f"Total corchetes abiertos: {total_CA}\n"
            result += f"Total corchetes cerrados: {total_CC}\n"
            result += f"Total error lexico: {total_ER}\n"
        else:
            result += f"No hay texto"
        return result

class LexerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ANALIZADOR LEXICO 😎")
        self.text_input = tk.Text(self.window, height=10, width=50)
        self.text_input.pack()

        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack()

        self.analyze_button = tk.Button(self.button_frame, text="Analizar", command=self.analyze_text)
        self.analyze_button.pack(side="left")

        self.clean_button = tk.Button(self.button_frame, text="Limpiar", command=self.clean_text)
        self.clean_button.pack(side="left")

        self.label_frame = tk.Frame(self.window)
        self.label_frame.pack()

        self.text_label = tk.Label(self.label_frame, text="Linea", anchor='w')
        self.text_label.pack(side="left")

        self.text_label = tk.Label(self.label_frame, text=" | Lexema | ", anchor='center')
        self.text_label.pack(side="left")

        self.text_label = tk.Label(self.label_frame, text="Token", anchor='e')
        self.text_label.pack(side="left")

        self.result_label = tk.Label(self.window, text=" ", height=0, width=65)
        self.result_label.pack()

        self.result_text = scrolledtext.ScrolledText(self.window, height=15, width=50, wrap=tk.WORD)
        self.result_text.pack()

    def analyze_text(self):
        lexer = Lexer()
        text = self.text_input.get("1.0", "end-1c")
        lines = text.split('\n')
        results = []

        for line_number, line in enumerate(lines, start=1):
            result_line = lexer.analyze(line)
            results.append(f"------------------------------------------------")
            results.append(f"{line_number} | {result_line}")  

        final_result = "\n".join(results)
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", final_result)

    def clean_text(self):
        self.text_input.delete("1.0", "end")
        self.result_label.config(text="")

    def run(self):
        self.window.mainloop()

app = LexerApp()
app.run()