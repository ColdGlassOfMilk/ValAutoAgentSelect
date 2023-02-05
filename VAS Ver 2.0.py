###############
#imports#
import time
import tkinter as tk
import tkinter.ttk as ttk
# from pygubu.widgets.combobox import Combobox
import pyautogui
import keyboard
from tkinter import PhotoImage
# from PIL import Image, ImageTk

#########################
# pyautogui settings
pyautogui.PAUSE = .001
pyautogui.FAILSAFE = True

#########################
#vars#
agent_slot_pos_dict = {
    "slot01" : [ 580,  920],
    "slot02" : [ 660,  920],
    "slot03" : [ 750,  920],
    "slot04" : [ 830,  920],
    "slot05" : [ 910,  920],
    "slot06" : [1000,  920],
    "slot07" : [1080,  920],
    "slot08" : [1170,  920],
    "slot09" : [1250,  920],
    "slot10" : [1350,  920],
    "slot11" : [ 580, 1000],
    "slot12" : [ 660, 1000],
    "slot13" : [ 750, 1000],
    "slot14" : [ 830, 1000],
    "slot15" : [ 910, 1000],
    "slot16" : [1000, 1000],
    "slot17" : [1080, 1000],
    "slot18" : [1170, 1000],
    "slot19" : [1250, 1000],
    "slot20" : [1350, 1000]
    }

#####################
#GUI#
class NewprojectApp:
    def __init__(self, master=None):
        self.selected_agent_pos = [580, 920]
        self.select_agent_button_pos = [960, 830]
        self.screen_res = 1

        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(height=430, width=350)
        toplevel1.geometry("430x350")
        toplevel1.wm_title("Valorant Auto Select Ver: 2.0")

        self.combobox1 = ttk.Combobox(toplevel1)
        self.combobox1.configure(values=["1080p", "1440p", "4k"])
        self.combobox1.pack(side="top")

        button1 = ttk.Button(toplevel1)
        button1.configure(text="Confirm Screen Res")
        button1.pack(side="top")
        button1.configure(command=self.on_button_res)

        self.combobox2 = ttk.Combobox(toplevel1)
        self.combobox2.configure(validate="none", values=list(agent_slot_pos_dict.keys()))
        self.combobox2.pack(side="top")

        button2 = ttk.Button(toplevel1)
        button2.configure(text="Confirm Agent")
        button2.pack(side="top")
        button2.configure(command=self.on_button_char)

        button3 = ttk.Button(toplevel1)
        button3.configure(text="Lock In")
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
        _text_ = (
            "DISCLAIMER:\n"
            "Use this softwear at your own risk. I do NOT take any responsibility for whatever happens to you or your account.\n"
            "\n"
            "Read the \"READ ME\" file to understand how to use this"
        )
        text1.insert("0.0", _text_)
        text1.pack(side="top")

###################
#Main widgets#
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()

    def on_button_res(self):
        value = self.combobox1.get()

        if value == "1080p":
            self.screen_res = 1
        elif value == "1440p":
            self.screen_res = 2
        elif value == "4k":
            self.screen_res = 4
        print(self.screen_res)

    def on_button_char(self):
        selected_char_val = self.combobox2.get()

        self.selected_agent_pos = agent_slot_pos_dict.get(selected_char_val, False);
        print(self.selected_agent_pos)

        if self.selected_agent_pos == False:
            print("Agent wasn't selected, agent set to \"agent01\"")
            self.select_agent_button_pos = agent_slot_pos_dict["slot01"]

    def on_lock_in(self):
        selected_char_val  = self.combobox2.get()

        # TODO: Do math to make program able to work on screens with different resolutions
        if self.screen_res == 1:
            pos = [x * 1 for x in self.selected_agent_pos]
            print(f"Screen res is: {self.screen_res} Selected char val is: {selected_char_val} \"selected_agent_pos\" value is: {self.selected_agent_pos} New position is: {pos}")
        elif self.screen_res == 2:
            pos = [x * 2 for x in self.selected_agent_pos]
            print(f"Screen res is: {self.screen_res} Selected char val is: {selected_char_val} \"selected_agent_pos\" value is: {self.selected_agent_pos} New position is: {pos}")
        elif self.screen_res == 4:
            pos = [x * 4 for x in self.selected_agent_pos]
            print(f"Screen res is: {self.screen_res} Selected char val is: {selected_char_val} \"selected_agent_pos\" value is: {self.selected_agent_pos} New position is: {pos}")
        else:
            print("Screen resolution wasn't set!")

        ######################
#loop#
        time.sleep(5)
        for i in range (10000):
            pyautogui.moveTo(self.selected_agent_pos)
            pyautogui.click()
            pyautogui.moveTo(self.select_agent_button_pos)
            pyautogui.click()
            #print("script has looped for:", i + 1, "Times")
            #print("<3")
            if keyboard.is_pressed("esc"):
                break

if __name__ == "__main__":
    app = NewprojectApp()
    app.run()
