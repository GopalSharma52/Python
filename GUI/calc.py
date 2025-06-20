from tkinter import *

# Basic Setup
window = Tk()
window.title("My First Calculator")
window.config(bg="white")
window.geometry("400x500")

expression = ""

# Function to handle button clicks
def press(num):
    global expression
    expression += str(num)
    entry.delete(0, END)
    entry.insert(0, expression)

def equalpress():
    global expression
    try:
        total = str(eval(expression))
        entry.delete(0, END)
        entry.insert(0, total)
        expression = total  # So you can continue calculating
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")
        expression = ""

def clear():
    global expression
    expression = ""
    entry.delete(0, END)

# Entry Widget
entry = Entry(window, width=22, font=('Arial', 20), bd=2, relief="ridge", justify="right")
entry.place(x=30, y=30)

# Button Specs: (text, x, y)
buttons = [
    ('7', 30, 100), ('8', 110, 100), ('9', 190, 100), ('/', 270, 100),
    ('4', 30, 160), ('5', 110, 160), ('6', 190, 160), ('*', 270, 160),
    ('1', 30, 220), ('2', 110, 220), ('3', 190, 220), ('-', 270, 220),
    ('C', 30, 280), ('0', 110, 280), ('=', 190, 280), ('+', 270, 280)
]

# Create Buttons
for (text, x, y) in buttons:
    if text == '=':
        Button(window, text=text, width=5, height=2, font=('Arial', 14), command=equalpress).place(x=x, y=y)
    elif text == 'C':
        Button(window, text=text, width=5, height=2, font=('Arial', 14), command=clear).place(x=x, y=y)
    else:
        Button(window, text=text, width=5, height=2, font=('Arial', 14), command=lambda t=text: press(t)).place(x=x, y=y)

window.mainloop()
