from tkinter import *
import socket
import threading

def windows_afegir_usuaris():
    ventana_afegir_usuaris = Toplevel()
    ventana_afegir_usuaris.geometry("600x300")
    ventana_afegir_usuaris.config(bg="#8cb3ff")
    ventana_afegir_usuaris.title("Afegir usuaris")
    ventana_afegir_usuaris.resizable(0,0)
    ventana_afegir_usuaris.geometry("+375+125")
    titol_usuaris = Label(ventana_afegir_usuaris, text="Afegir usuaris", font=("THIN", 18, "bold"), bg="#8cb3ff")
    titol_usuaris.place(x=62, y=45)
    introduir_nom_usuari = Label(ventana_afegir_usuaris, text="Introdueix el nom de l'usuari", font=("THIN", 16), bg="#8cb3ff")
    introduir_nom_usuari.place(x=17, y= 100)
    nom_afegir_usuari = Entry(ventana_afegir_usuaris, font=("Calibri", 16), borderwidth=1, relief="solid", bg="#ffee04")
    nom_afegir_usuari.place(x=35, y=150)
    boto_afegir_usuaris = Button(ventana_afegir_usuaris, text="Afegeix", fg="#ffee04",bg="#606fff", cursor="hand2",font=("Calibri", 13, "bold"),width=14, borderwidth=0)
    boto_afegir_usuaris.place(x=78,y=210 )
    imatge_usuari = PhotoImage(file="contactes.png")
    tamany_imatge = imatge_usuari.subsample(2)
    imatge_ventana = Label(ventana_afegir_usuaris, image=tamany_imatge, bg="#8cb3ff")
    imatge_ventana.place(x=330, y=10)
    ventana_afegir_usuaris.mainloop()

def validacio_conta(name, password):
    if name == "admin" and password == "admin":
        root.destroy()
        chat_ventana_funcion()

def chat_ventana_funcion():
    chat_ventana = Tk()
    chat_ventana.title("Clogin")
    chat_ventana.geometry("1131x668")
    chat_ventana.resizable(0, 0)

    # Frame Lateral --------------------------------------------------------------------------------------------

    frame_lateral = Frame(chat_ventana, bg="#057fbc", width=270, height=668, borderwidth=2, relief="solid")
    frame_lateral.place(x=0)

    photo_logo_clogin = PhotoImage(file="logo.png")
    photo_logo_clogin = photo_logo_clogin.subsample(22)
    logo_clogin = Label(frame_lateral, image=photo_logo_clogin, borderwidth=0, bg="#057fbc")
    logo_clogin.place(x=0, y=0)

    nom_clogin = Label(frame_lateral, text="CLOGIN", font=("Calibri", 12, "bold"), bg="#057fbc", fg="#ffffff")
    nom_clogin.place(x=40, y=11)

    line_clogin_sota = Frame(frame_lateral, width=266, height=2, bg="#A9CAE8")
    line_clogin_sota.place(x=0, y=80)

    imagen_ajustes_generales_button = PhotoImage(file="botoajustes.png")
    imagen_ajustes_generales_button = imagen_ajustes_generales_button.subsample(23)
    ajustes_generales_button = Button(frame_lateral, image=imagen_ajustes_generales_button, borderwidth=0, bg="#057fbc", cursor="hand2", activebackground="#057fbc")
    ajustes_generales_button.place(x=230, y=10)

    foto_afegir_contactes = PhotoImage(file="adduser.png")
    foto_afegir_contactes = foto_afegir_contactes.subsample(23)
    afegir_contactes = Button(frame_lateral, image=foto_afegir_contactes, borderwidth=0, bg="#057fbc", cursor="hand2", activebackground="#057fbc", command=windows_afegir_usuaris)
    afegir_contactes.place(x=195, y=10)

    label_tu_cuenta = Label(frame_lateral, text="Has iniciat sessió amb:", font=("THIN", 13, "bold"), bg="#057fbc", fg="#ffffff")
    label_tu_cuenta.place(x=42, y=45)

    foto_usuari_perfil_lateral = PhotoImage(file="second_foto.png")
    foto_usuari_perfil_lateral = foto_usuari_perfil_lateral.subsample(13)
    usuari_foto = Label(frame_lateral, image=foto_usuari_perfil_lateral, borderwidth=0, bg="#057fbc")
    usuari_foto.place(x=25, y=90)

    my_name = Label(frame_lateral, text="Your Name", font=("Calibri", 15, "bold"), bg="#057fbc")
    my_name.place(x=120, y=110)

    # ----------------------------------------------------------------------------------------------------------

    # Frame Conversa -------------------------------------------------------------------------------------------

    frame_conversa = Frame(chat_ventana, bg="#ffffff", width=863, height=668, borderwidth=2, relief="solid")
    frame_conversa.place(x=268)

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

def registredesessio():
    global inpconfirmaciocontrasenya
    global inpcontrasenya
    global ventana
    root.destroy()
    ventana = Tk()
    ventana.geometry("400x600")
    ventana.geometry("+475+50")
    ventana.resizable(0,0)
    ventana.title("Registra't")
    ventana.config(bg="#FFFFFF")

    logoclogin = PhotoImage(file="logo.png")
    zoom_logo = logoclogin.subsample(7)
    photo = Label(ventana, image=zoom_logo, bg="#FFFFFF")
    photo.place(x=125, y=0)

    nomusuari = Label(ventana, text="Nom d'usuari", font=("THIN", 16), bg="#FFFFFF")
    nomusuari.place(x=135, y=170)

    password = Label(ventana, text="Contrasenya", font=("THIN", 16), bg="#FFFFFF")
    password.place(x=135, y=260)

    inpnom = Entry(ventana, font=("Calibri", 18), width=28, borderwidth=1, relief="solid", bg="#ffee04")
    inpnom.place(x=28, y=205)

    inpcontrasenya = Entry(ventana, font=("Calibri", 18), width=28, borderwidth=1, relief="solid", bg="#ffee04")
    inpcontrasenya.place(x=28, y=295)
    inpcontrasenya.config(show="*")

    confirmaciopassword = Label(ventana, text="Repeteix la contrasenya", font=("THIN", 16), bg="#FFFFFF")
    confirmaciopassword.place(x=80, y=360)

    inpconfirmaciocontrasenya = Entry(ventana, font=("Calibri", 18), width=28, borderwidth=1, relief="solid", bg="#ffee04")
    inpconfirmaciocontrasenya.place(x=28, y=395)
    inpconfirmaciocontrasenya.config(show="*")

    botonsingup = Button(ventana, text="Registra't", fg="#ffee04", bg="#606fff", cursor="hand2", font=("Calibri", 15, "bold"), width=18, borderwidth=0, command=confirmacio_contrasenya, activebackground="#ffff98", activeforeground="#606fff")
    botonsingup.place(x=108, y=475)

    imatgeenrere = PhotoImage(file="enrere.png")
    imatgeenrere = imatgeenrere.subsample(10)

    enrere = Button(ventana, command=inicidesessio, image = imatgeenrere, borderwidth=0, bg="#FFFFFF", cursor="hand2")
    enrere.place(x=12, y=20)

    ventana.mainloop()

def inicidesessio():
    global root
    try:
        ventana.destroy()
    except:
        pass
    root = Tk()
    root.geometry("400x600")
    root.geometry("+475+50")
    root.resizable(0,0)
    root.title("Iniciar sessió")
    root.config(bg="#FFFFFF")
    
    logo_clogin = PhotoImage(file="logo.png")
    zoom = logo_clogin.subsample(7)
    foto = Label(root, image=zoom, bg="#FFFFFF")
    foto.place(x=125, y=0)

    nom_usuari = Label(root, text="Nom d'usuari", font=("THIN", 16), bg="#FFFFFF")
    nom_usuari.place(x=135, y=165)

    contrasenya = Label(root, text="Contrasenya", font=("THIN", 16), bg="#FFFFFF")
    contrasenya.place(x=135, y=265)

    inp_nom = Entry(root, font=("Calibri", 18), width=28, borderwidth=1, relief="solid", bg="#ffee04")
    inp_nom.place(x=28, y=200)

    inp_contrasenya = Entry(root, font=("Calibri", 18), width=28, borderwidth=1, relief="solid", bg="#ffee04")
    inp_contrasenya.place(x=28, y=300)
    inp_contrasenya.config(show="*")

    boton_singup = Button(root, text="Entra", fg="#ffee04", bg="#606fff", cursor="hand2", font=("Calibri", 15, "bold"), width=18, borderwidth=0, activebackground="#ffff98", activeforeground="#606fff", command=lambda:validacio_conta(inp_nom.get(), inp_contrasenya.get()))
    boton_singup.place(x=105, y=370)

    lab_register = Label(root, text="No tens compte?", font=("THIN", 14, "underline"), bg="#FFFFFF")
    lab_register.place(x=35, y=530)

    button_register = Button(root, text="Registra't", fg="#ffee04", bg="#606fff", cursor="hand2", font=("Calibri", 15, "bold"), width=16, borderwidth=0, command=registredesessio, activebackground="#ffff98", activeforeground="#606fff")
    button_register.place(x=195, y=525)
    
    root.mainloop()

def confirmacio_contrasenya():
    respostaconfirmacio = inpconfirmaciocontrasenya.get()
    respostacontrasenya = inpcontrasenya.get()

    if respostaconfirmacio != respostacontrasenya:
        error = Label(ventana, text="Les contrasenyes no coincideixen", font=("Calibri", 12, "bold"), fg="red", bg="#FFFFFF")
        error.place(x= 88, y= 430)  

inicidesessio()

