import tkinter as tk
import math

window = tk.Tk()
window.title("Calculator")
window.resizable(0, 0)

frame_text = tk.Frame(master=window, width=250,
                      height=50, bd=0, highlightthickness=0)
frame_text.pack(fill=tk.BOTH,  side=tk.TOP, expand=True)

# Buttons Method


def bt_clear():
    global expression
    expression = ""
    input_text.set("")
    # text.setvar(value="")


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = result


def btn_percentage():
    global expression
    result = str(eval(expression)*0.01)
    input_text.set(result)
    expression = result


def btn_sqroot():
    global expression
    result = math.sqrt(int(expression))
    input_text.set(str(result))
    expression = result


def close_win(e):
    window.destroy()


expression = ""
input_text = tk.StringVar()

text = tk.Entry(master=frame_text, width=15, bg="#3B4252", foreground="#f7f7f7", bd=0,
                highlightthickness=0, textvariable=input_text, font=("Sans", 26), justify="right")
text.grid(row=0, column=0)
text.pack(fill=tk.BOTH, side=tk.TOP, expand=True, ipady=10)

# Buttons
frame_buttons = tk.Frame(master=window, width=250, height=250, bg="#2C2C2C")
frame_buttons.pack(fill=tk.BOTH,  side=tk.BOTTOM, expand=True)

# Opertaion buttons
clear = tk.Button(master=frame_buttons, text="C", font=("Sans", 18), bg="#A21223", fg="#f7f7f7", bd=0, highlightthickness=0,
                  width=4, height=2, activebackground="#3C3C3C", cursor="hand2", activeforeground="#f7f7f7", command=lambda: bt_clear())
clear.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

divide = tk.Button(master=frame_buttons, text="/", font=("Sans", 18), bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                   width=4, height=2, activebackground="#3C3C3C", cursor="hand2", activeforeground="#f7f7f7", command=lambda: btn_click("/"))
divide.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)

percentage = tk.Button(master=frame_buttons, text="%", font=("Sans", 18), bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                       width=4, height=2, activebackground="#3C3C3C", cursor="hand2", activeforeground="#f7f7f7", command=lambda: btn_percentage())
percentage.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)

multiply = tk.Button(master=frame_buttons, font=("Sans", 18), text="*", bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                     width=4, height=2, activebackground="#3C3C3C", activeforeground="#f7f7f7", cursor="hand2", command=lambda: btn_click("*"))
multiply.grid(row=0, column=3, sticky="nsew", padx=2, pady=2)

subtract = tk.Button(master=frame_buttons, font=("Sans", 18), text="-", bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                     width=4, height=2, activebackground="#3C3C3C", activeforeground="#f7f7f7", cursor="hand2", command=lambda: btn_click("-"))
subtract.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)

add = tk.Button(master=frame_buttons, font=("Sans", 18), text="+", bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                width=4, height=2, activebackground="#3C3C3C", activeforeground="#f7f7f7", cursor="hand2", command=lambda: btn_click("+"))
add.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)

sqroot = tk.Button(master=frame_buttons, text="sqrt", font=("Sans", 18), bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                   width=4, height=2, activebackground="#3C3C3C", cursor="hand2", activeforeground="#f7f7f7", command=lambda: btn_sqroot())
sqroot.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)

dot = tk.Button(master=frame_buttons, text=".", font=("Sans", 18), bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                width=4, height=2, activebackground="#3C3C3C", cursor="hand2", activeforeground="#f7f7f7", command=lambda: btn_click("."))
dot.grid(row=4, column=2, sticky="nsew", padx=2, pady=2)

equal = tk.Button(master=frame_buttons, font=("Sans", 18), text="=", bg="#0D761D", fg="#f7f7f7", bd=0, highlightthickness=0,
                  width=4, height=2, activebackground="#3C3C3C", activeforeground="#f7f7f7", cursor="hand2", command=lambda: bt_equal())
equal.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)

# Number buttons
btn1 = tk.Button(master=frame_buttons, font=("Sans", 18), text="1", bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                 width=4, height=2, activebackground="#3C3C3C", activeforeground="#f7f7f7", cursor="hand2", command=lambda: btn_click("1"))
btn1.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)

btn2 = tk.Button(master=frame_buttons, font=("Sans", 18), text="2", bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                 width=4, height=2, activebackground="#3C3C3C", activeforeground="#f7f7f7", cursor="hand2", command=lambda: btn_click("2"))
btn2.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)

btn3 = tk.Button(master=frame_buttons, font=("Sans", 18), text="3", bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                 width=4, height=2, activebackground="#3C3C3C", activeforeground="#f7f7f7", cursor="hand2", command=lambda: btn_click("3"))
btn3.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)

btn4 = tk.Button(master=frame_buttons, font=("Sans", 18), text="4", bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                 width=4, height=2, activebackground="#3C3C3C", activeforeground="#f7f7f7", cursor="hand2", command=lambda: btn_click("4"))
btn4.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)

btn5 = tk.Button(master=frame_buttons, font=("Sans", 18), text="5", bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                 width=4, height=2, activebackground="#3C3C3C", activeforeground="#f7f7f7", cursor="hand2", command=lambda: btn_click("5"))
btn5.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)

btn6 = tk.Button(master=frame_buttons, font=("Sans", 18), text="6", bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                 width=4, height=2, activebackground="#3C3C3C", activeforeground="#f7f7f7", cursor="hand2", command=lambda: btn_click("6"))
btn6.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)

btn7 = tk.Button(master=frame_buttons, font=("Sans", 18), text="7", bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                 width=4, height=2, activebackground="#3C3C3C", activeforeground="#f7f7f7", cursor="hand2", command=lambda: btn_click("7"))
btn7.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

btn8 = tk.Button(master=frame_buttons, font=("Sans", 18), text="8", bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                 width=4, height=2, activebackground="#3C3C3C", activeforeground="#f7f7f7", cursor="hand2", command=lambda: btn_click("8"))
btn8.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)

btn9 = tk.Button(master=frame_buttons, font=("Sans", 18), text="9", bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                 width=4, height=2, activebackground="#3C3C3C", activeforeground="#f7f7f7", cursor="hand2", command=lambda: btn_click("9"))
btn9.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)

btn0 = tk.Button(master=frame_buttons, font=("Sans", 18), text="0", bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                 width=4, height=2, activebackground="#3C3C3C", activeforeground="#f7f7f7", cursor="hand2", command=lambda: btn_click("0"))
btn0.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)

btn00 = tk.Button(master=frame_buttons, font=("Sans", 18), text="00", bg="#373737", fg="#f7f7f7", bd=0, highlightthickness=0,
                  width=4, height=2, activebackground="#3C3C3C", activeforeground="#f7f7f7", cursor="hand2", command=lambda: btn_click("0"))
btn00.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)


window.bind('<Escape>', lambda e: close_win(e))
window.mainloop()
