###############
import time
import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.combobox import Combobox
import pyautogui
import keyboard
from tkinter import PhotoImage
from PIL import Image, ImageTk
#########################
pyautogui.PAUSE = .001
pyautogui.FAILSAFE = True
#########################
#agent positions#
select_agent = [960, 830]
slot1 = [580, 920]
slot2 = [660, 920]
slot3 = [750, 920]
slot4 = [830, 920]
slot5 = [910, 920]
slot6 = [1000, 920]
slot7 = [1080,920]
slot8 = [1170, 920]
slot9 = [1250, 920]
slot10 = [1350, 920]
slot11 = [580, 1000]
slot12 = [660, 1000]
slot13 = [750, 1000]
slot14 = [830, 1000]
slot15 = [910, 1000]
slot16 = [1000, 1000]
slot17 = [1080, 1000]
slot18 = [1170, 1000]
slot19 = [1250, 1000]
slot20 = [1350, 1000]
a = 920
b = 1000
#####################


#####################
screen_res = int
char_val = ['slot1', 'slot2', 'slot3', 'slot4', 'slot5', 'slot6', 'slot7', 'slot8', 'slot9', 'slot10', 'slot11', 'slot12', 'slot13', 'slot14', 'slot15', 'slot16', 'slot17', 'slot18', 'slot19', 'slot20', 'slot21']
#pos = ""
piss = ""
selected_char_val = str







class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(height=430, width=350)
        toplevel1.geometry("430x350")
        toplevel1.wm_title("Valorant Auto Select Ver:1.0")
        self.combobox1 = Combobox(toplevel1)
        self.combobox1.configure(values='1080p 1440p 4k')
        self.combobox1.pack(side="top")
        button1 = ttk.Button(toplevel1)
        button1.configure(text='Confirm Screen Res')
        button1.pack(side="top")
        button1.configure(command=self.on_button_res)
        self.combobox2 = ttk.Combobox(toplevel1)
        self.combobox2.configure(validate="none", values='slot1 slot2 slot3 slot4 slot5 slot6 slot7 slot8 slot9 slot10 slot11 slot12 slot13 slot14 slot15 slot16 slot17 slot18 slot19 slot20')
        self.combobox2.pack(side="top")
        button2 = ttk.Button(toplevel1)
        button2.configure(text='Confirm Agent')
        button2.pack(side="top")
        button2.configure(command=self.on_button_char)
        button3 = ttk.Button(toplevel1)
        button3.configure(text='Lock In')
        button3.pack(side="top")
        button3.configure(command=self.on_lock_in)
        text1 = tk.Text(toplevel1)
        text1.configure(
            borderwidth=5,
            cursor="arrow",
            exportselection="true",
            height=10,
            insertunfocussed="none",
            relief="raised",
            setgrid="false",
            state="normal",
            tabstyle="tabular",
            takefocus=True,
            undo="false")
        _text_ = 'DISCLAIMER:\nUse this softwear at your own risk. I do NOT take any responsibility for whatever happens to you or your account.\n\nRead the "READ ME" file to understand how to use this'
        text1.insert("0.0", _text_)
        text1.pack(side="top")

###################
        
        
        
        
####################


########################
        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()

    def on_button_res(self):
        global screen_res
        value = self.combobox1.get()
        if value == "1080p":
            screen_res = 1
        elif value == "1440p":
            screen_res = 2
        elif value == "4k":
            screen_res = 4
        print(screen_res)
        
        
        
    def on_button_char(self):
        global selected_char_val
        global char_val
        global a
        global b
        global piss
        selected_char_val = self.combobox2.get()
        #hehe....piss var 
        if selected_char_val == 'slot1':
            piss = [580, a]
        elif selected_char_val == 'slot2':
            piss = [660, a]
        elif selected_char_val == 'slot3':
            piss = [750, a]
        elif selected_char_val == 'slot4':
            piss = [830, a]
        elif selected_char_val == 'slot5':
            piss = [910, a]
        elif selected_char_val == 'slot6':
            piss = [b, a]
        elif selected_char_val == 'slot7':
            piss = [1080, a]
        elif selected_char_val == 'slot8':
            piss = [1170, a]
        elif selected_char_val == 'slot9':
            piss = [1250, a]
        elif selected_char_val == 'slot10':
            piss = [1350, a]
        elif selected_char_val == 'slot11':
            piss = [580, b]
        elif selected_char_val == 'slot12':
            piss = [660, b]
        elif selected_char_val == 'slot13':
            piss = [750, b]
        elif selected_char_val == 'slot14':
            piss = [830, b]
        elif selected_char_val == 'slot15':
            piss = [910, b]
        elif selected_char_val == 'slot16':
            piss = [b, b]
        elif selected_char_val == 'slot17':
            piss = [1080, b]
        elif selected_char_val == 'slot18':
            piss = [1170, b]
        elif selected_char_val == 'slot19':
            piss = [1250,b]
        elif selected_char_val == 'slot20':
            piss = [1350,b]
        print(piss)


    def on_lock_in(self):
        global screen_res
        global char_val
        global selected_char_val
        global pos
        global piss
        #lets just add all the fucking variables while we're at it until it works -_-
        if screen_res == 1:
            pos = [x * 1 for x in piss]
            print("screen res is:", screen_res, selected_char_val, piss, pos)
        elif screen_res == 2:
            pos = [x * 2 for x in piss]
            print("screen_res is", screen_res, selected_char_val, piss, pos)
        elif screen_res == 4:
            pos = [x * 4 for x in piss]
            print("screen_res is", screen_res,"selected char val is", selected_char_val,"piss value is", piss,"new position is", pos)
        else:
            print("nothing here")
        
        i = 1
        time.sleep(5)
        for i in range (10000):
            pyautogui.moveTo(piss)
            pyautogui.click()
            pyautogui.moveTo(select_agent)
            pyautogui.click()
            print("script has looped for:", i + 1, "Times")
            print("<3")
            if keyboard.is_pressed('esc'):
                break




    
if __name__ == "__main__":
    app = NewprojectApp()
    app.run()
