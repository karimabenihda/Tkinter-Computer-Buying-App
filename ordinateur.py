from tkinter import *
import ttkbootstrap as tkb
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.geometry('900x600')

#__________________________definir les fonctions utilisée________________________________
def appliquer_reduction():
    prix_initial = float(prixentry.get())
    statut = categorieentry.get()
    reduction = 0
    if statut == "Etudiant":
        reduction = 0.8  #pour les étudiants (1 - 0.2)
    else:
        reduction = 0.9  # pour les autres

    prix_reduit = prix_initial *  reduction

    reductionentry.delete(0, 'end')  # Efface le contenu actuel de reductionentry
    reductionentry.insert(0, f"{prix_reduit:.2f} DH")  # Insère la réduction calculée dans reductionentry

def calculate_total():
    selected_item = cartentry.get()
    if selected_item in cart_prices:
        item_value = cart_prices[selected_item]
        total_var.set(total_var.get() + item_value + choix1.get() + choix2.get())

#__________________________l'interface________________________________

title=Label(root,text="CONSTITUER VOTRE PC",font=("Arial",18)).place(x=300,y=0)

cart_prices={
    "ASSUS":700,
    "VIA":600,
    "SIS":500
}

#combobox
cart=(Label(root,text="Cart mère :",font=("Arial",14),bg="#255C6F"))
cart.place(x=150,y=30)
cartentry=(ttk.Combobox(root,values=list(cart_prices.keys())))
cartentry.place(x=300,y=30)

#radiobutton
ecran=Label(root,text="Ecran :",font=("Arial",14)).place(x=150,y=60)
Taille=Label(root,text="Taille :").place(x=200,y=100)
Type=Label(root,text="type :").place(x=200,y=140)

choix1 = IntVar()
plat=(Radiobutton(root,text="Plat :", variable=choix1, value="1000"))
plat.place(x=250,y=100)
cathodique=(Radiobutton(root,text="Cathodique :", variable=choix1, value="500"))
cathodique.place(x=300,y=100)

choix2 =IntVar()
type1=(Radiobutton(root,text='15"', variable=choix2, value="1000"))
type1.place(x=250,y=140)
type2=(Radiobutton(root,text='17"', variable=choix2, value="999"))
type2.place(x=300,y=140)

frame=Frame(root).pack(padx=20, pady=10)

#checkbutton
option=Label(root,text="Options :",font=("Arial",14),bg="green").place(x=150,y=180)

c=Checkbutton(root,text="Carte Satellite",onvalue=900,offvalue=0).place(x=250,y=220)
i=Checkbutton(root,text="Imprimante",onvalue=600,offvalue=0).place(x=250,y=260)
s=Checkbutton(root,text="Scanner",onvalue=600,offvalue=0).place(x=250,y=300)

#button&prix
total_var = IntVar()
btn=Button(root,text="Calculer le prix",width=50, command=calculate_total).place(x=150,y=340)

prixlabel=(Label(root,text="Ce PC vous Coùtera :").place(x=270,y=380))
prixentry=(Entry(root, state='readonly', textvariable=total_var,width=50))
prixentry.place(x=250,y=420)

#categories&reduction appliquée
categorie=Label(root,text="Catégorie :",font=("Arial",14),bg="#255C6F").place(x=150,y=460)
categorieentry=(ttk.Combobox(root,values=["Autre","Etudiant"]))
categorieentry.place(x=250,y=500)

reductionlabel=Label(root,text="Taux de réduction correspondant : ")
reductionlabel.place(x=420,y=500)
reductionentry=Entry(root,width=30)
reductionentry.place(x=609,y=500)


categorieentry.bind("<<ComboboxSelected>>", lambda event: appliquer_reduction())
root.mainloop()

