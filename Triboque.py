import tkinter
from tkinter import *
from tkinter import ttk

import select

# from customtkinter import *


window = Tk()
window.geometry("600x400")
window.resizable(False, False)
window.config(background="grey")
window.title("Triboque, software na stanovení kyselosti oleje.")

# Definice barev a písma
main_font = ("Helvetica", 12)
vysledek_font = ("Helvetica", 16)
main_color = "#b29bc2"

# Záložky programu
nb = ttk.Notebook(window)
nb.place(x=0, y=0, width=600, height=400)
tab1 = tkinter.Frame(window, borderwidth=1, highlightcolor="black", background=main_color)
nb.add(tab1, text="Stanovení kyselosti")
tab2 = tkinter.Frame(window, borderwidth=1, highlightcolor="black", background=main_color)
nb.add(tab2, text="Roztoky")
tab3 = tkinter.Frame(window, borderwidth=1, highlightcolor="black", background=main_color)
nb.add(tab3, text="O programu")

nb.select(tab2)
nb.enable_traversal()

# Logo
logo = PhotoImage(file="img/sumixon130x50_black.png")
# Vzorec
vzorec = PhotoImage(file="img/vzorec.png")
# Piknometr
piknometr = PhotoImage(file="img/pikno100x145.png")


# Funkce
# Global funkce
def prevod(entry):
    text = entry.get()
    if text.__contains__(","):
        return float(text.replace(",", "."))
    else:
        return float(text)


# Stanovení kyselosti
def vypocitej():
    # EQ1 - spotřeba titru
    eq1 = prevod(eq1_entry)
    # B - Blank
    b = prevod(b_entry)
    # T - koncetrace titru
    t = prevod(t_entry)
    # M - molární hmotnost
    m = prevod(mol_entry)
    # Hmotnost oleje
    v = prevod(v_entry)
    # Index
    f1 = prevod(f1_entry)

    # výpočet
    tan = round(((eq1 - b) * t * m * f1) / (v * f1), 3)
    vysledek_label["text"] = tan


def vypocitej_enter(event):
    # EQ1 - spotřeba titru
    eq1 = prevod(eq1_entry)
    # B - Blank
    b = prevod(b_entry)
    # T - koncetrace titru
    t = prevod(t_entry)
    # M - molární hmotnost
    m = prevod(mol_entry)
    # V - Hmotnost oleje
    v = prevod(v_entry)
    # Index
    f1 = prevod(f1_entry)

    # výpočet enter
    tan = round(((eq1 - b) * t * m * f1) / (v * f1), 3)
    vysledek_label["text"] = tan


# Entr pro výpočet
window.bind("<Return>", vypocitej_enter)


# ---Rozpracováno-------------------------------------------------------------------
# tab = nb.tab('current')['text']
# print(tab)
# if tab == "Stanovení kyselosti":

# def on_tab_change():
#     tab = nb.tab('current')['text']
#     if tab == "Stanovení kyselosti":
#         window.bind("<Return>", vypocitej_enter)
#
#
# nb.bind('<<NotebookTabChanged>>', on_tab_change())
# -------------------------------------------------------------------------------
# Funkce
# Roztoky

def hustota():
    # Hmotnost 1
    m0_text = m0_entry.get()
    if m0_text.__contains__(","):
        m0 = float(m0_text.replace(",", "."))
    else:
        m0 = float(m0_text)
    # Hmotnost 2
    m1_text = m1_entry.get()
    if m1_text.__contains__(","):
        m1 = float(m1_text.replace(",", "."))
    else:
        m1 = float(m1_text)
    # Rozdíl hmotností

    mm = round(m1 - m0, 4)
    m_entry["text"] = mm
    print(m0)
    print(m1)
    print(mm)

    # hodnota s dropdown menu
    objem = float(vaha.get())
    print(objem)

    # výpočet hustoty
    hustota = round(mm / objem, 3)

    vysledek_label1["text"] = f"{hustota} g/cm3"


# Framy

main_frame1 = LabelFrame(tab1, borderwidth=0, highlightcolor="black", background=main_color)
main_frame1.place(x=0, y=60, width=600, height=350)

main_frame2 = LabelFrame(tab2, borderwidth=0, highlightcolor="black", background=main_color)
main_frame2.place(x=0, y=50, width=600, height=350)

main_frame3 = LabelFrame(tab3, borderwidth=0, highlightcolor="black", background=main_color)
main_frame3.place(x=0, y=50, width=600, height=350)

# Definování prvků

# Název a logo labels

logo_label = Label(tab1, image=logo, height=50, width=130, borderwidth=0, justify=RIGHT)
logo_label.place(x=470, y=0)
logo_label = Label(tab2, image=logo, height=50, width=130, borderwidth=0, background=main_color)
logo_label.place(x=470, y=0)
logo_label = Label(tab3, image=logo, height=50, width=130, borderwidth=0)
logo_label.place(x=470, y=0)
nazev_label_tab1 = Label(tab1, text="Stanovení čísla kyselosti.", font=("Helvetica", 22), background=main_color)
nazev_label_tab1.place(x=5, y=5)
nazev_label_tab2 = Label(tab2, text="Stanovení hustoty roztoku.", font=("Helvetica", 22), background=main_color)
nazev_label_tab2.place(x=5, y=5)

# Proměnné labels
# ######TAB1########

eq1_label = Label(main_frame1, text="EQ1", background=main_color, font=main_font, padx=25, pady=5)
eq1_label.grid(row=0, column=0)

b_label = Label(main_frame1, text="B", background=main_color, font=main_font, pady=5)
b_label.grid(row=1, column=0)

t_label = Label(main_frame1, text="T", background=main_color, font=main_font, padx=5, pady=5)
t_label.grid(row=2, column=0)

m_label = Label(main_frame1, text="M", background=main_color, font=main_font, padx=5, pady=5)
m_label.grid(row=3, column=0)

v_label = Label(main_frame1, text="V", background=main_color, font=main_font, padx=5, pady=5)
v_label.grid(row=4, column=0)

f1_label = Label(main_frame1, text="F1", background=main_color, font=main_font, padx=5, pady=5)
f1_label.grid(row=5, column=0)

# Proměnné labels
# ######TAB2########

m0_label = Label(main_frame2, text="m0", background=main_color, font=main_font, padx=25, pady=5)
m0_label.grid(row=0, column=0, sticky=W)

m1_label = Label(main_frame2, text="m1", background=main_color, font=main_font, padx=25, pady=5)
m1_label.grid(row=1, column=0, sticky=W)

m_label = Label(main_frame2, text="m", background=main_color, font=main_font, padx=25, pady=5)
m_label.grid(row=2, column=0, sticky=W)

# Vstupy proměnných
# ######TAB1########

eq1_entry = Entry(main_frame1, background=main_color, font=main_font, width=15, justify=CENTER)
eq1_entry.grid(row=0, column=1)

b_entry = Entry(main_frame1, background=main_color, font=main_font, width=15, justify=CENTER)
b_entry.grid(row=1, column=1)

t_entry = Entry(main_frame1, background=main_color, font=main_font, width=15, justify=CENTER)
t_entry.grid(row=2, column=1)

mol_entry = Entry(main_frame1, background=main_color, font=main_font, width=15, justify=CENTER)
mol_entry.insert(0, 56.1)
mol_entry.grid(row=3, column=1)

v_entry = Entry(main_frame1, background=main_color, font=main_font, width=15, justify=CENTER)
v_entry.grid(row=4, column=1)

f1_entry = Entry(main_frame1, background=main_color, font=main_font, width=15, justify=CENTER)
f1_entry.insert(0, "1")
f1_entry.grid(row=5, column=1)

# Vstupy proměnných
# ######TAB2########

m0_entry = Entry(main_frame2, background=main_color, font=main_font, width=15, justify=CENTER)
m0_entry.grid(row=0, column=1)

m1_entry = Entry(main_frame2, background=main_color, font=main_font, width=15, justify=CENTER)
m1_entry.grid(row=1, column=1)

m_entry = Label(main_frame2, background=main_color, font=main_font, width=15, justify=CENTER,
                highlightthickness=1, highlightbackground="black")
m_entry.grid(row=2, column=1)

# Popisy proměnných
# ######TAB1########

eq1_label = Label(main_frame1, text="Spotřeba titru v bodě ekvivalence (ml)", background=main_color, font=main_font,
                  padx=15, pady=5)
eq1_label.grid(row=0, column=2)

b_label = Label(main_frame1, text="Blank (ml)", background=main_color, font=main_font, padx=15, pady=5)
b_label.grid(row=1, column=2, sticky=W)

t_label = Label(main_frame1, text="Koncentrace titru (mol/l)", background=main_color, font=main_font, padx=15, pady=5)
t_label.grid(row=2, column=2, sticky=W)

m_label = Label(main_frame1, text="Molární hmotnost titru (g/mol)", background=main_color, font=main_font, padx=15,
                pady=5)
m_label.grid(row=3, column=2, sticky=W)

v_label = Label(main_frame1, text="Hmotnost oleje (g)", background=main_color, font=main_font, padx=15, pady=5)
v_label.grid(row=4, column=2, sticky=W)

f1_label = Label(main_frame1, text="Faktor", background=main_color, font=main_font, padx=15, pady=5)
f1_label.grid(row=5, column=2, sticky=W)

# Popisy proměnných
# ######TAB2########

m0_label = Label(main_frame2, text="Hmotnost suchého piknometru (g)", background=main_color, font=main_font,
                 padx=15, pady=5)
m0_label.grid(row=0, column=2, sticky=W)

m1_label = Label(main_frame2, text="Hmotnost pinkometru s kapalinou (g)", background=main_color, font=main_font,
                 padx=15, pady=5)
m1_label.grid(row=1, column=2, sticky=W)

m_label = Label(main_frame2, text="Rozdíl váhy m1 - m0", background=main_color, font=main_font, padx=15, pady=5)
m_label.grid(row=2, column=2, sticky=W)

# Img
# ######TAB2########

vzorec_label = Label(main_frame2, image=vzorec, background=main_color, pady=10)
vzorec_label.place(x=270, y=100)
piknometr_label = Label(main_frame2, image=piknometr, background=main_color)
piknometr_label.place(x=480, y=120)

# Dropdownmenu
# ######TAB2########
parametry = [
    u"10",
    u"20",
    u"30",
    u"50",
    u"100"
]
vaha = StringVar(main_frame2)
vaha.set(parametry[0])
piknom = OptionMenu(main_frame2, vaha, *parametry)
piknom.config(font=main_font, bg=main_color, fg="black", pady=5, padx=5, bd=1,
              activebackground=main_color, activeforeground='blue', width=4, borderwidth=0, highlightbackground="black",
              highlightthickness=1, relief="sunken")
piknom.place(x=250, y=250)

drop_label = Label(main_frame2, text="Zvolte objem piknometru ! (ml)", background=main_color, font=main_font,
                   padx=15, pady=5)
drop_label.place(x=230, y=210)

# Button
# ######TAB1########

start_button = Button(main_frame1, borderwidth=2, text="Vypočítej", bg=main_color, activebackground=main_color, padx=15,
                      pady=15,
                      font=main_font, overrelief="solid", highlightthickness=1, highlightbackground=main_color,
                      command=vypocitej)
start_button.grid(row=6, column=0, padx=15, pady=15)

# Button
# ######TAB2########
start_button1 = Button(main_frame2, borderwidth=2, text="Vypočítej", bg=main_color, activebackground=main_color,
                       padx=15, pady=15, font=main_font, overrelief="solid", highlightthickness=1,
                       highlightbackground=main_color, command=hustota
                       )
start_button1.place(x=28, y=190)

# Výsledek labels
# ######TAB1########

vysledek_label = Label(main_frame1, text="", background=main_color, font=main_font, padx=15, pady=5,
                       highlightthickness=1, highlightbackground="black", width=12)
vysledek_label.grid(row=6, column=1, sticky=W)

vysledek_popis_label = Label(main_frame1, text="mg KOH / 1g oleje", background=main_color, font=main_font, padx=15,
                             pady=5)
vysledek_popis_label.grid(row=6, column=2, sticky=W)

# Výsledek labels
# ######TAB2########
vysledek_label1 = Label(main_frame2, text=" ", background=main_color, font=vysledek_font, padx=0, pady=15,
                        highlightthickness=1, highlightbackground="black", width=16)
vysledek_label1.place(x=28, y=120)

window.mainloop()
