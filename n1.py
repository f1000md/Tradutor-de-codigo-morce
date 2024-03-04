import tkinter as tk
from tkinter import messagebox

def calcular_media():
    try:
        n1 = float(entrada_n1.get())
        Av1 = float(entrada_av1.get())
        Av2 = float(entrada_av2.get())
        Tra = float(entrada_tra.get())

        media = (Av1 * 1.5 + Av2 * 1.2 + Tra * 1.0) / 3

        resultado = f"Média: {media:.1f}"
        if media >= n1:
            resultado += "\nSituação: Aprovado"
        else:
            rec = float(entrada_rec.get())
            media2 = (media + rec) / 2
            if media2 >= n1:
                resultado += f"\nSituação após recuperação: Aprovado com média {media2:.1f}"
            else:
                resultado += f"\nSituação após recuperação: Reprovado com média {media2:.1f}"

        messagebox.showinfo("Resultado", resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criando a janela principal
root = tk.Tk()
root.title("Cálculo de Média")

# Criando e posicionando os elementos na janela
tk.Label(root, text="Média da Escola:").grid(row=0, column=0)
entrada_n1 = tk.Entry(root)
entrada_n1.grid(row=0, column=1)

tk.Label(root, text="Nota Av1:").grid(row=1, column=0)
entrada_av1 = tk.Entry(root)
entrada_av1.grid(row=1, column=1)

tk.Label(root, text="Nota Av2:").grid(row=2, column=0)
entrada_av2 = tk.Entry(root)
entrada_av2.grid(row=2, column=1)

tk.Label(root, text="Nota do Trabalho:").grid(row=3, column=0)
entrada_tra = tk.Entry(root)
entrada_tra.grid(row=3, column=1)

tk.Label(root, text="Nota de Recuperação:").grid(row=4, column=0)
entrada_rec = tk.Entry(root)
entrada_rec.grid(row=4, column=1)

btn_calcular = tk.Button(root, text="Calcular Média", command=calcular_media)
btn_calcular.grid(row=5, columnspan=2)

# Iniciando o loop da interface
root.mainloop()