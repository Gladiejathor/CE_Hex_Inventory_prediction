#this programm calculates the next 3 hex numbers in the sequence
# Path: HexRechner.py


# Import the necessary modules
import tkinter as tk
from tkinter import *
# import math calculations for hex numbers
import math as math
# import the necessary modules for the calculation of the next hex number
import re as re
import operator as op
import functools as ft

#define global variables in float type for the calculation of the next hex number
global hex_number_1
global hex_number_2
global hex_number_3
global hex_number_4
hex_number_4 = float(0x0)
global hex_number_5
hex_number_5 = float(0x0)

#get input from the user through the textbox1 and textbox2 textbox3 for hex_number_1 and hex_number_2
def get_input():
    global hex_number_1
    global hex_number_2
    global hex_number_3
    hex_number_1 = float(textbox1.get())
    hex_number_2 = float(textbox2.get())
    hex_number_3 = float(textbox3.get())
    return hex_number_1, hex_number_2, hex_number_3
#check if the input is a hex number
def is_hex_number(hex_number):
    hex_number = str(hex_number)
    if re.match(r'^[0-9a-fA-F]+$', hex_number):
        return True
    else:
        return False
#if is_hex_number is false, the user has to enter a valid hex number showing the error message
def check_hex_number():
    if is_hex_number(hex_number_1) == False:
        error_message_1.config(text="Please enter a valid hex number")
        return False
    elif is_hex_number(hex_number_2) == False:
        error_message_2.config(text="Please enter a valid hex number")
        return False
    elif is_hex_number(hex_number_3) == False:
        error_message_3.config(text="Please enter a valid hex number")
        return False
    else:
        return True
#calculate the sequence between hex_number_1 and hex_number_2 and hex_number_3 using the functools module
def calculate_sequence():
    global hex_number_4
    global hex_number_5
    hex_number_4 = ft.reduce(op.add, [hex_number_1, hex_number_2, hex_number_3])
    hex_number_5 = ft.reduce(op.add, [hex_number_2, hex_number_3, hex_number_4])
    return hex_number_4, hex_number_5


# Create the main window
root = tk.Tk()
root.title("Hex Rechner")
root.geometry("300x300")
root.resizable(0, 0)
root.configure(background='#50f950')
# add 3 textboxes and discription labels to the textboxes
textbox1 = tk.Entry(root, width=10)
textbox1.grid(row=0, column=1)
textbox2 = tk.Entry(root, width=10)
textbox2.grid(row=1, column=1)
textbox3 = tk.Entry(root, width=10)
textbox3.grid(row=2, column=1)
label1 = tk.Label(root, text="Hex1")
label1.grid(row=0, column=0)
label2 = tk.Label(root, text="Hex2", background='#50f950')
label2.grid(row=1, column=0)
label3 = tk.Label(root, text="Hex3")
label3.grid(row=2, column=0)
# add 2 copyble textes to the window containing the string carsted from hex_number_4 and hex_number_5
# text for containg the variables hex_number_4 and hex_number_5
# textbox4 and textbox5 insert hex_number_4 and hex_number_5
textbox4 = tk.Entry(root, width=10)
textbox4.grid(row=3, column=1)
textbox5 = tk.Entry(root, width=10)
textbox5.grid(row=4, column=1)
#carst hex_number_4 and hex_number_5 into intergers
textbox4.insert(0, int(hex_number_4))
textbox5.insert(0, int(hex_number_5))

# textbox4.insert(0, hex(hex_number_4))
# textbox5.insert(0, hex(hex_number_5))


# add a button to the main window to close the window down right
button1 = tk.Button(root, text="Close", command=root.destroy)
button1.grid(row=5, column=4)
# add a button to the main window to calculate the next hex number
button2 = tk.Button(root, text="Calculate", command=get_input)
button2.grid(row=5, column=1)
# add a button to the main window to copy the next hex number to the clipboard
button3 = tk.Button(root, text="Copy", command=lambda: root.clipboard_append(textbox4.get()))
button3.grid(row=5, column=2)
# add a button to the main window to copy the next hex number to the clipboard
button4 = tk.Button(root, text="Copy", command=lambda: root.clipboard_append(textbox5.get()))
button4.grid(row=5, column=3)
# add a label to the main window to show the error message if the user has entered an invalid hex number
error_message_1 = tk.Label(root, text="", background='#50f950')
error_message_1.grid(row=0, column=2)
error_message_2 = tk.Label(root, text="", background='#50f950')
error_message_2.grid(row=1, column=2)
error_message_3 = tk.Label(root, text="", background='#50f950')
error_message_3.grid(row=2, column=2)

mainloop()



#alternative lösung:
'''
#calculate the next hex number in the sequence
def calculate_next_hex_number():
    global hex_number_1
    global hex_number_2
    global hex_number_3
    global hex_number_4
    global hex_number_5
    hex_number_1, hex_number_2, hex_number_3 = get_input()
    if check_hex_number() == True:
        calculate_sequence()
        hex_number_4 = hex(hex_number_4)
        hex_number_5 = hex(hex_number_5)
        hex_number_4 = hex_number_4[2:]
        hex_number_5 = hex_number_5[2:]
        hex_number_4 = hex_number_4.upper()
        hex_number_5 = hex_number_5.upper()
        hex_number_4 = float(hex_number_4)
        hex_number_5 = float(hex_number_5)
        hex_number_4 = hex_number_4.hex()
        hex_number_5 = hex_number_5.hex()
        hex_number_4 = float(hex_number_4)
        hex_number_5 = float(hex_number_5)
        textbox4.delete(0, END)
        textbox5.delete(0, END)
        textbox4.insert(0, hex_number_4)
        textbox5.insert(0, hex_number_5)
        return hex_number_4, hex_number_5
'''