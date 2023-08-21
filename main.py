import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import rembg
import numpy as np

def remover_fundo():
    # Abre uma janela de diálogo para selecionar uma imagem
    file_path = filedialog.askopenfilename()
    
    if file_path:
        # Carrega a imagem usando a biblioteca PIL
        image = Image.open(file_path)
        
        # Converte a imagem em um formato aceitável pela rembg
        image_array = np.array(image)
        output = rembg.remove(image_array)
        
        # Converte a saída de rembg de volta para uma imagem PIL
        output_image = Image.fromarray(output)
        
        # Salva a imagem com o fundo removido
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            output_image.save(save_path)
        
        # Atualiza a imagem exibida na interface
        photo = ImageTk.PhotoImage(output_image)
        label.config(image=photo)
        label.image = photo

# Cria a janela principal
root = tk.Tk()
root.title("Remover Fundo de Imagem e Salvar")

# Cria um rótulo para exibir a imagem
label = tk.Label(root)
label.pack(padx=10, pady=10)

# Cria um botão para iniciar a remoção do fundo e salvar a imagem
remover_button = tk.Button(root, text="Remover Fundo e Salvar", command=remover_fundo)
remover_button.pack(pady=10)

# Inicia o loop principal da interface gráfica
root.mainloop()
