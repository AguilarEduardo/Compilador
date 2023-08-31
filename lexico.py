import tkinter as tk

class Lexer:
    def __init__(self):
        self.delimiters = [".", ";"]
        self.keywords = ["public", "static", "void", "main", "int"]
        self.operators = ["=", "+", "-", "*", "/"]
        self.numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.apertura = ['(']
        self.cierre = [')']
        self.llaveA = ['{']
        self.llaveB = ['}']

    def is_valid_identifier(self, token):
        return token == "n" or (token.isalpha() and token != "main" and token != "int")

    def tokenize(self, text):
        self.tokens = self.delimiters + self.keywords + self.operators + self.numbers + self.apertura + self.cierre + self.llaveA + self.llaveB
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
        contadorD = 0
        contadorP = 0
        contadorO = 0
        contadorN = 0
        contadorI = 0
        contadorPA = 0
        contadorPC = 0
        contadorLA = 0
        contadorLC = 0
        contadorEL = 0
        for token in arreglo:
            if token in self.delimiters:
                result += f"{token} | Delimitador\n"
                contadorD+=1
            elif token in self.keywords:
                result += f"{token} | Palabra reservada\n"
                contadorP+=1
            elif token in self.operators:
                result += f"{token} | Operador\n"
                contadorO+=1
            elif token in self.numbers:
                result += f"{token} | Número\n"
                contadorN+=1
            elif self.is_valid_identifier(token):
                result += f"{token} | Identificador\n"
                contadorI+=1
            elif token in self.apertura:
                result += f"{token} | Parentecis de apertura\n"
                contadorPA+=1
            elif token in self.cierre:
                result += f"{token} | Parentecis de cierre\n"
                contadorPC+=1
            elif token in self.llaveA:
                result += f"{token} | Llave de apertura\n"
                contadorLA+=1
            elif token in self.llaveB:
                result += f"{token} | Llave de cierre\n"
                contadorLC+=1
            else:
                result += f"{token} | Error lexico x_x\n"
                contadorEL+=1
        result += f"Numero total de Delimitador: {contadorD}\n"
        result += f"Numero total de palabras reservadas: {contadorP}\n"
        result += f"Numero total de Operadores: {contadorO}\n"
        result += f"Numero total de Numeros: {contadorN}\n"
        result += f"Numero total de Identificadores: {contadorI}\n"
        result += f"Numero total de Parentecis abierto: {contadorPA}\n"
        result += f"Numero total de Parentecis cerrado: {contadorPC}\n"
        result += f"Numero total de Llave abierta: {contadorLA}\n"
        result += f"Numero total de Llave cerrada: {contadorLC}\n"
        result += f"Numero total de Error Lexico: {contadorEL}\n"
        return result


class LexerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ANALIZADOR LEXICO 😎")
        self.text_input = tk.Text(self.window, height=10, width=50)
        self.text_input.pack()

        self.analyze_button = tk.Button(self.window, text="Analizar", command=self.analyze_text)
        self.analyze_button.pack()

        self.clean_button = tk.Button(self.window, text="Limpiar", command=self.clean_text)
        self.clean_button.pack()

        frame = tk.Frame(self.window)
        frame.pack()

        self.text_label = tk.Label(frame, text="Linea", anchor='w')
        self.text_label.pack(side="left")

        self.text_label = tk.Label(frame, text=" | Lexema | ", anchor='center')
        self.text_label.pack(side="left")

        self.text_label = tk.Label(frame, text="Token | ", anchor='e')
        self.text_label.pack(side="left")

        self.text_label = tk.Label(frame, text="Suma", anchor='e')
        self.text_label.pack(side="left")


        self.result_label = tk.Label(self.window, text=" ", height=35, width=50)
        self.result_label.pack()


    def analyze_text(self):
        lexer = Lexer()
        text = self.text_input.get("1.0", "end-1c")  # Corregido para evitar el último salto de línea
        lines = text.split('\n')
        results = []

        for line_number, line in enumerate(lines, start=1):
            result_line = lexer.analyze(line)
            results.append(f"{line_number} | {result_line}")

        final_result = "\n".join(results)
        self.result_label.config(text=final_result)


    def clean_text(self):
        self.text_input.delete("1.0", "end")
        self.result_label.config(text="")

    def run(self):
        self.window.mainloop()

    def run(self):
        self.window.mainloop()
app = LexerApp()
app.run()