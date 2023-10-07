import tkinter as tk 

def convertir():
    try:

        kilometros = float(entrada_kilometros.get())

   
        millas=kilometros*0.621371

        
        etiqueta_resultado.config(text=f"{kilometros}kilometros son {millas}millas")
    except ValueError:
        
        etiqueta_resultado.config(text="ingrese un valor numerico valido")

ventana=tk.Tk()
ventana.title("convettidor de kilometros a millas")
ventana.geometry("300x150") 


etiqueta_instrucion = tk.Label(ventana, text="ingrese la distancia en kilometros:")
etiqueta_instrucion.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entrada_kilometros= tk.Entry(ventana)
entrada_kilometros.grid(row=1, column=0, padx=10, pady=10)
                        
boton_convertir=tk.Button(ventana, text="convertir", command=convertir)
boton_convertir.grid(row=1, column=1, padx=10, pady=10)

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
