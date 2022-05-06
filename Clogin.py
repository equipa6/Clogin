from tkinter import *
import socket
import threading

chat_ventana = Tk()
chat_ventana.title("Clogin")
chat_ventana.geometry("1131x668")

frame_superior = Frame(chat_ventana, bg="#909497", width=866, height=90, borderwidth=2, relief="solid")
frame_superior.place(x=265)

frame_lateral = Frame(chat_ventana, bg="#057fbc", width=270, height=668, borderwidth=2, relief="solid")
frame_lateral.place(x=0)

frame_conversa = Frame(chat_ventana, bg="#ffffff", width=863, height=580, borderwidth=2, relief="solid")
frame_conversa.place(x=268, y=88)

inp_chat = Entry(frame_conversa, font=("THIN", 19), bg="#2C3E50", fg="#ffffff", width=55, borderwidth=0)
inp_chat.place(x=0, y=546)

send_button = Button(frame_conversa, font=("THIN", 13), bg="#1A5276", text=">>", borderwidth=0, width=9)
send_button.place(x=772, y=546)

frame_per_omplir_boto = Frame(frame_conversa, bg="#1A5276", borderwidth=3, width=87)
frame_per_omplir_boto.place(x=772, y=575)







chat_ventana.mainloop()