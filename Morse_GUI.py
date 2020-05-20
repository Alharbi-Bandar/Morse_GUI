

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time

RPi.GPIO.setwarnings(False)
RPi.GPIO.setmode(RPi.GPIO.BCM)

ledpin= LED(18)


win = Tk()
win.title("Converting to Morse Code by GUI")
varFont = tkinter.font.Font(family = 'Times New Roman' , size = 16, weight = "bold")

def line():
    ledpin.on()
    time.sleep(1)
    ledpin.off()
    time.sleep(0.5)

def dot():
    ledpin.on()
    time.sleep(0.5)
    ledpin.off()
    time.sleep(0.5)
    

def convert_taxt_To_Code():
    MorseCode = { 
        'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.','F': '..-.',
        'G': '--.','H': '....','I': '..','J': '.---','K': '-.-','L': '.-..',
        'M': '--','N': '-.','O': '---','P': '.--.','Q': '--.-','R': '.-.',
        'S': '...','T': '-','U': '..-','V': '...-','W': '.--','X': '-..-',
        'Y': '-.--','Z': '--..',
        '0': '-----','1': '.----','2': '..---','3': '...--','4': '....-',
        '5': '.....','6': '-....','7': '--...','8': '---..','9': '----.' }
        
    Morse_code_Text = text_entry.get()
    if len(Morse_code_Text) > 12:
        print('You have wrong Entry')
        return
    for index_1 in Morse_code_Text:
            for index_2 in MorseCode[index_1.upper()]:
                
                if index_2 == '-':
                    line()
                    
                elif index_2 == '.':
                    dot()
                    
                else:
                    time.sleep(0.5)
            time.sleep(0.5)


def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
text_entry = Entry(win, text='Enter_Valid_Name', width=50, bg="yellow")
text_entry.grid(row=1,column=3)

redButton = Button(win, text='Submit', font=varFont, command=convert_taxt_To_Code, bg='green', height=2, width=28)
redButton.grid(row=3,column=3)

exitButton = Button(win, text='Exit', font=varFont, command=close, bg='red', height=2, width=11)
exitButton.grid(row=5, column=3)

win.protocol("WM_DELETE_WINDOW", close)  

win.mainloop() 

