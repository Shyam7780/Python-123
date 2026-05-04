import tkinter as tk

def click(event):
    global expression
    expression += str(event.widget["text"])
    screen_var.set(expression)

def clear():
    global expression
    expression = ""
    screen_var.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        screen_var.set(result)
        expression = result
    except:
        screen_var.set("Error")
        expression = ""

root = tk.Tk()
root.title("Calculator")

expression = ""
screen_var = tk.StringVar()

screen = tk.Entry(root, textvar=screen_var, font="Arial 20", bd=10, relief=tk.RIDGE)
screen.pack(fill=tk.BOTH, ipadx=8)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

for button in buttons:
    btn = tk.Button(frame, text=button, font="Arial 15", width=5, height=2)
    btn.grid(row=row, column=col)
    
    if button == "=":
        btn.config(command=calculate)
    else:
        btn.bind("<Button-1>", click)

    col += 1
    if col > 3:
        col = 0
        row += 1

clear_btn = tk.Button(root, text="Clear", command=clear, font="Arial 15")
clear_btn.pack(fill=tk.BOTH)

root.mainloop()