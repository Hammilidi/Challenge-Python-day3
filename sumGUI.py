import tkinter as tk
import tkinter.font as font

#*****************    fonctions    *************************************************************
def calculSum():
    value1 = float(entry1.get())
    value2 = float(entry2.get())
    sum= value1 + value2
    resulat_label.config(text=f"Le somme de {value1} et {value2} est: {sum}")

def calculSubstract():
    value1 = float(entry1.get())
    value2 = float(entry2.get())
    substract = value1 - value2
    resulat_label.config(text=f"Le soustraction de {value1} et {value2} est: {substract}")

def calculMultiply():
    value1 = float(entry1.get())
    value2 = float(entry2.get())
    multiply = value1 * value2
    resulat_label.config(text=f"Le produit de {value1} et {value2} est: {multiply}")

def calculDivide():
    value1 = float(entry1.get())
    value2 = float(entry2.get())
    divide = value1 / value2
    resulat_label.config(text=f"Le division de {value1} et {value2} est: {divide}")
    

#************  Interface graphique   *******************************************************

root=tk.Tk()
root.title("Calculator")
root.geometry("400x400")
root.configure(bg="#E1D5D3")
#definir une police
f = font.Font(family='Times New Roman')
#entry
entry1=tk.Entry(root)
entry1.place(relwidth=0.3,relheight=0.1, relx=0.1, rely=0.015)

entry2=tk.Entry()
entry2.place(relwidth=0.3, relx=0.1, relheight=0.1, rely=0.2)

#sum button
sumButton=tk.Button(root, text="+", command=calculSum)
sumButton.place(relx=0.7, rely=0.01, relwidth=0.2) 
sumButton["font"]=f

#substract button
substractButton=tk.Button(root, text="-", command=calculSubstract)
substractButton.place(relx=0.7, rely=0.08, relwidth=0.2)

#Multiply button
substractButton=tk.Button(root, text="*", command=calculMultiply)
substractButton.place(relx=0.7, rely=0.16, relwidth=0.2)

#divide button
substractButton=tk.Button(root, text="/", command=calculDivide)
substractButton.place(relx=0.7, rely=0.24, relwidth=0.2)

#Label for displaying result
resulat_label=tk.Label(root, text="Le résultat est:")
resulat_label.place(relx=0.3, rely=0.32, relheight=0.2)

#Quit button
quitButton=tk.Button(root, text="Quit", command=root.destroy)
quitButton.place(relx=0.35, rely=0.6, relwidth=0.3)


root.mainloop()