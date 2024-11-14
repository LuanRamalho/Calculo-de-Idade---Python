import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calcular_idade():
    data_nascimento_str = entrada_data.get()
    try:
        # Converte a string da data para um objeto datetime
        data_nascimento = datetime.strptime(data_nascimento_str, "%d-%m-%Y")
        hoje = datetime.now()
        
        # Calcula a diferença
        anos = hoje.year - data_nascimento.year
        meses = hoje.month - data_nascimento.month
        dias = hoje.day - data_nascimento.day

        # Ajusta os meses e dias se necessário
        if dias < 0:
            meses -= 1
            dias += (data_nascimento.replace(month=data_nascimento.month % 12 + 1, day=1) - data_nascimento.replace(month=data_nascimento.month, day=1)).days
        
        if meses < 0:
            anos -= 1
            meses += 12

        # Exibe a idade
        resultado = f"Idade: {anos} anos, {meses} meses e {dias} dias."
        messagebox.showinfo("Resultado", resultado)

    except ValueError:
        messagebox.showerror("Erro", "Data inválida. Utilize o formato DD-MM-YYYY.")

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Calculador de Idade")
janela.geometry("300x200")
janela.resizable(False, False)

# Estilo da interface
janela.configure(bg="#f0f0f0")

# Label e entrada de data
label = tk.Label(janela, text="Digite sua data de nascimento:", bg="#f0f0f0")
label.pack(pady=10)

entrada_data = tk.Entry(janela, font=("Arial", 14))
entrada_data.pack(pady=10)

# Botão para calcular a idade
botao_calcular = tk.Button(janela, text="Calcular Idade", command=calcular_idade, bg="#4CAF50", fg="white", font=("Arial", 12))
botao_calcular.pack(pady=20)

# Inicia o loop da interface
janela.mainloop()
