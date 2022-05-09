from cProfile import label
from tkinter import *
import socket
import threading
from turtle import bgcolor, width

chat_ventana = Tk()
chat_ventana.title("Clogin")
chat_ventana.geometry("1131x668")
chat_ventana.resizable(0, 0)

# FRAME DE LES CONFIGURACIONS GENERALS----------------------------------------------------------------------
"""
frame_superior = Frame(chat_ventana, bg="#909497", width=866, height=90, borderwidth=2, relief="solid")
frame_superior.place(x=265)

photo_logo_clogin = PhotoImage(file="logo.png")
photo_logo_clogin = photo_logo_clogin.subsample(12)
logo_clogin = Label(frame_superior, image=photo_logo_clogin, borderwidth=0, bg="#909497")
logo_clogin.place(x=310)

nom_clogin = Label(frame_superior, text="CLOGIN", font=("Calibri", 23, "bold"), bg="#909497")
nom_clogin.place(x=385, y=20)

ajustes_button = PhotoImage(file="botoajustes.png")
ajustes_button = ajustes_button.subsample(15)
label_ajustes_button = Button(frame_superior, image=ajustes_button, borderwidth=0, bg="#909497")
label_ajustes_button.place(x=800, y=25)
"""

# ----------------------------------------------------------------------------------------------------------

# Frame Lateral --------------------------------------------------------------------------------------------

frame_lateral = Frame(chat_ventana, bg="#057fbc", width=270, height=668, borderwidth=2, relief="solid")
frame_lateral.place(x=0)

photo_logo_clogin = PhotoImage(file="logo.png")
photo_logo_clogin = photo_logo_clogin.subsample(14)
logo_clogin = Label(frame_lateral, image=photo_logo_clogin, borderwidth=0, bg="#057fbc")
logo_clogin.place(x=45, y=1)

nom_clogin = Label(frame_lateral, text="CLOGIN", font=("Calibri", 18, "bold"), bg="#057fbc")
nom_clogin.place(x=110, y=21)

# ----------------------------------------------------------------------------------------------------------

# Frame Conversa -------------------------------------------------------------------------------------------

frame_conversa = Frame(chat_ventana, bg="#ffffff", width=863, height=668, borderwidth=2, relief="solid")
frame_conversa.place(x=268)

frame_usuari = Frame(frame_conversa, bg="#61758B", width=859, height=80, borderwidth=0)
frame_usuari.place(x=0)

nom_usuari = Label(frame_usuari, bg="#61758B", text="Usuari", font=("Calibri", 20, "bold"))
nom_usuari.place(x=70, y=18)

foto_usuari_perfil = PhotoImage(file="foto_perfil.png")
foto_usuari_perfil = foto_usuari_perfil.subsample(10)
usuari_foto = Label(frame_usuari, image=foto_usuari_perfil, borderwidth=0, bg="#61758B")
usuari_foto.place(x=12, y=12)

inp_chat = Entry(frame_conversa, font=("THIN", 19), bg="#2C3E50", fg="#ffffff", width=55, borderwidth=0)
inp_chat.place(x=0, y=634)

send_button = Button(frame_conversa, font=("THIN", 13), bg="#1A5276", text=">>", borderwidth=0, width=9)
send_button.place(x=772, y=634)

frame_per_omplir_boto = Frame(frame_conversa, bg="#1A5276", borderwidth=3, width=87)
frame_per_omplir_boto.place(x=772, y=663)

ajustes_button = PhotoImage(file="tres_punts.png")
ajustes_button = ajustes_button.subsample(19)
label_ajustes_button = Menubutton(frame_usuari, image=ajustes_button, borderwidth=0, bg="#61758B")
label_ajustes_button.place(x=810, y=25)
menu = Menu(label_ajustes_button, tearoff=False, bg="#61758B", fg="#ffffff")
menu.add_radiobutton(label="Bloquejar", font=("Calibri", 13, "bold"))
menu.add_radiobutton(label="Arxivar", font=("Calibri", 13, "bold"))
menu.add_radiobutton(label="Ancorar", font=("Calibri", 13, "bold"))
label_ajustes_button["menu"] = menu



# ----------------------------------------------------------------------------------------------------------


chat_ventana.mainloop()