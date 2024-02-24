import tkinter
from tkinter import *
from tkinter import ttk

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
def vypocitej():
    # EQ1 - spotřeba titru
    eq1_text = eq1_entry.get()
    if eq1_text.__contains__(","):
        eq1 = float(eq1_text.replace(",", "."))
    else:
        eq1 = float(eq1_text)
    # B - Blank
    b_text = b_entry.get()
    if b_text.__contains__(","):
        b = float(b_text.replace(",", "."))
    else:
        b = float(b_text)
    # T - koncetrace titru
    t_text = t_entry.get()
    if t_text.__contains__(","):
        t = float(t_text.replace(",", "."))
    else:
        t = float(t_text)
    # M - molární hmotnost
    m = 56.1

    v_text = v_entry.get()
    if v_text.__contains__(","):
        w = float(v_text.replace(",", "."))
    else:
        w = float(v_text)
    f1_text = f1_entry.get()
    if f1_text.__contains__(","):
        f1 = float(f1_text.replace(",", "."))
    else:
        f1 = float(f1_text)

    # výpočet

    tan = round(((eq1 - b) * t * m * f1) / (w * f1), 2)

    vysledek_label["text"] = tan


def vypocitej_enter(event):
    # EQ1 - spotřeba titru
    eq1_text = eq1_entry.get()
    if eq1_text.__contains__(","):
        eq1 = float(eq1_text.replace(",", "."))
    else:
        eq1 = float(eq1_text)
    # B - Blank
    b_text = b_entry.get()
    if b_text.__contains__(","):
        b = float(b_text.replace(",", "."))
    else:
        b = float(b_text)
    # T - koncetrace titru
    t_text = t_entry.get()
    if t_text.__contains__(","):
        t = float(t_text.replace(",", "."))
    else:
        t = float(t_text)
    # M - molární hmotnost
    m_text = m_entry.get()
    if m_text.__contains__(","):
        m = float(m_text.replace(",", "."))
    else:
        m = float(m_text)
    # W - Hmotnost oleje
    v_text = v_entry.get()
    if v_text.__contains__(","):
        w = float(v_text.replace(",", "."))
    else:
        v = float(v_text)
    f1_text = f1_entry.get()
    if f1_text.__contains__(","):
        f1 = float(f1_text.replace(",", "."))
    else:
        f1 = float(f1_text)

    # výpočet enter

    tan = round(((eq1 - b) * t * m * f1) / (v * f1), 2)

    vysledek_label["text"] = tan


# Entr pro výpočet

window.bind("<Return>", vypocitej_enter)

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

m1_label = Label(main_frame2, text="m1", background=main_color, font=main_font, padx=25, pady=5)
m1_label.grid(row=0, column=0, sticky=W)

m2_label = Label(main_frame2, text="m2", background=main_color, font=main_font, padx=25, pady=5)
m2_label.grid(row=1, column=0, sticky=W)

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

m_entry = Entry(main_frame1, background=main_color, font=main_font, width=15, justify=CENTER)
m_entry.insert(0, "56.1")
m_entry.grid(row=3, column=1)

v_entry = Entry(main_frame1, background=main_color, font=main_font, width=15, justify=CENTER)
v_entry.grid(row=4, column=1)

f1_entry = Entry(main_frame1, background=main_color, font=main_font, width=15, justify=CENTER)
f1_entry.insert(0, "1")
f1_entry.grid(row=5, column=1)

# Vstupy proměnných
# ######TAB2########

m1_entry = Entry(main_frame2, background=main_color, font=main_font, width=15, justify=CENTER)
m1_entry.grid(row=0, column=1)

m2_entry = Entry(main_frame2, background=main_color, font=main_font, width=15, justify=CENTER)
m2_entry.grid(row=1, column=1)

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

m1_label = Label(main_frame2, text="Hmotnost suchého piknometru (g)", background=main_color, font=main_font,
                 padx=15, pady=5)
m1_label.grid(row=0, column=2, sticky=W)

m2_label = Label(main_frame2, text="Hmotnost pinkometru s kapalinou (g)", background=main_color, font=main_font,
                 padx=15, pady=5)
m2_label.grid(row=1, column=2, sticky=W)

m_label = Label(main_frame2, text="Rozdíl váhy m2 -m1", background=main_color, font=main_font, padx=15, pady=5)
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
    u"10ml",
    u"20ml",
    u"30ml",
    u"50ml",
    u"100ml"
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
                       highlightbackground=main_color,
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
vysledek_label1 = Label(main_frame2, text="huráhurá", background=main_color, font=vysledek_font, padx=0, pady=15,
                        highlightthickness=1, highlightbackground="black", width=16)
vysledek_label1.place(x=28, y=120)

window.mainloop()
