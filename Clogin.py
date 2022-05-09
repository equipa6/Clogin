from cProfile import label
from email.mime import image
from tkinter import *
import socket
import threading
from turtle import bgcolor, width

chat_ventana = Tk()
chat_ventana.title("Clogin")
chat_ventana.geometry("1131x668")
chat_ventana.resizable(0, 0)

# Frame Lateral --------------------------------------------------------------------------------------------

frame_lateral = Frame(chat_ventana, bg="#057fbc", width=270, height=668, borderwidth=2, relief="solid")
frame_lateral.place(x=0)

photo_logo_clogin = PhotoImage(file="logo.png")
photo_logo_clogin = photo_logo_clogin.subsample(20)
logo_clogin = Label(frame_lateral, image=photo_logo_clogin, borderwidth=0, bg="#057fbc")
logo_clogin.place(x=60, y=0)

nom_clogin = Label(frame_lateral, text="CLOGIN", font=("Calibri", 15, "bold"), bg="#057fbc", fg="#ffffff")
nom_clogin.place(x=110, y=10)

line_clogin_sota = Frame(frame_lateral, width=266, height=2, bg="black")
line_clogin_sota.place(x=0, y=50)

imagen_ajustes_generales_button = PhotoImage(file="botoajustes.png")
imagen_ajustes_generales_button = imagen_ajustes_generales_button.subsample(20)
ajustes_generales_button = Button(frame_lateral, image=imagen_ajustes_generales_button, borderwidth=0, bg="#057fbc", cursor="hand2", activebackground="#057fbc")
ajustes_generales_button.place(x=230, y=60)

foto_afegir_contactes = PhotoImage(file="adduser.png")
foto_afegir_contactes = foto_afegir_contactes.subsample(20)
afegir_contactes = Button(frame_lateral, image=foto_afegir_contactes, borderwidth=0, bg="#057fbc", cursor="hand2", activebackground="#057fbc")
afegir_contactes.place(x=195, y=60)

# ----------------------------------------------------------------------------------------------------------

# Frame Conversa -------------------------------------------------------------------------------------------

frame_conversa = Frame(chat_ventana, bg="#ffffff", width=863, height=668, borderwidth=2, relief="solid")
frame_conversa.place(x=268)

canvas_convera = Canvas(frame_conversa, width=855, height=550, borderwidth=0)
canvas_convera.place(x=0,y=70)

bg = PhotoImage(file="fondo2.png")
si = Label(canvas_convera, image=bg)
si.place(x=0, y=20)



frame_usuari = Frame(frame_conversa, bg="#4682B4", width=859, height=80, borderwidth=0)
frame_usuari.place(x=0)

nom_usuari = Label(frame_usuari, bg="#4682B4", text="Usuari", font=("Calibri", 20, "bold"))
nom_usuari.place(x=70, y=18)

foto_usuari_perfil = PhotoImage(file="foto_perfil.png")
foto_usuari_perfil = foto_usuari_perfil.subsample(10)
usuari_foto = Label(frame_usuari, image=foto_usuari_perfil, borderwidth=0, bg="#4682B4")
usuari_foto.place(x=12, y=12)

inp_chat = Entry(frame_conversa, font=("THIN", 19), bg="#2C3E50", fg="#ffffff", width=55, borderwidth=0)
inp_chat.place(x=0, y=634)

send_button = Button(frame_conversa, font=("THIN", 13), bg="#1A5276", text=">>", borderwidth=0, width=9)
send_button.place(x=772, y=634)

frame_per_omplir_boto = Frame(frame_conversa, bg="#1A5276", borderwidth=3, width=87)
frame_per_omplir_boto.place(x=772, y=663)

ajustes_button = PhotoImage(file="tres_punts.png")
ajustes_button = ajustes_button.subsample(19)
label_ajustes_button = Menubutton(frame_usuari, image=ajustes_button, borderwidth=0, bg="#4682B4", activebackground="#4682B4", cursor="hand2")
label_ajustes_button.place(x=810, y=25)
menu = Menu(label_ajustes_button, tearoff=False, bg="#61758B", fg="#ffffff")
menu.add_radiobutton(label="Bloquejar", font=("Calibri", 13, "bold"))
menu.add_radiobutton(label="Arxivar", font=("Calibri", 13, "bold"))
menu.add_radiobutton(label="Ancorar", font=("Calibri", 13, "bold"))
label_ajustes_button["menu"] = menu

# ----------------------------------------------------------------------------------------------------------


chat_ventana.mainloop()