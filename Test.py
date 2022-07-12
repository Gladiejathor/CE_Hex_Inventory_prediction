#x = int(3)
#i = int(7)
from importlib import import_module


x, i, p = 3, 2, 0

# for x in range(10):
#     x = x+1
#     i = i+i
#     print(i)


#jetzt for von 200 zu 1000 testen       range(start, bis, schrittweite)
## for x in range(200, 1000, 1):
for x in range(200, 1000, 100):
    p = p+1
    print(p)

print("ClaownFish.")
print(x)
print(i)
print(p)
print("")
print("")
print("")

q = hex(i)
print(q)

#dann testen oder es in einem URL-String als veriable ersetzt werden kann.

# some ez AWT

"""
import tkinter as tk
from time import sleep

def getvalue():

    value = "haha"

    sleep(3)

    return value

def printvalue():

    value = getvalue()

    print(value)

app = tk.Tk()
app.geometry("500x300")
button = tk.Button(app, text="Var1 hier lachen", command=printvalue)
button.pack()

app.mainloop()
"""
# gleicher code wie oben nur aufgeräumter
"""
import tkinter as tk

def getvalue():
    return "haha"

def second_part(other):
    print('after delay')

    value = getvalue()

    # code moved from first part
    print('value:', value)
    print('other:', other)
    button['text'] = value #nonsens ?

def print_value():
    # first part makes some calculation
    other_variable = 'kommt vom knopf'

    print('before delay')

    # run function with delay and send all data from first part
    app.after(3000, second_part, other_variable)

    # rest of code moved to second_part

app = tk.Tk()

button = tk.Button(app, text="var 2 hier kichern", command=print_value)
button.pack()

app.mainloop()
"""

