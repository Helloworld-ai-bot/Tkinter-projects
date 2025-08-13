import tkinter as tk
import math


numlist = []
Symbol = ""
a5 = 0
a4 = 0
a3 = 0
a2 = 0
a1 = 0

root = tk.Tk()

root.title('calculator')

width_of_calculator = round(root.winfo_screenwidth()/2.436)
height_of_calculator = round(root.winfo_screenheight()/1.317)
root.geometry(f"{width_of_calculator}x{height_of_calculator}")
root.resizable(False,False)
root.config(bg = '#06202B')

e1 = tk.Text(root, background='#FCFAED',width=49,height=4,cursor="arrow",font=("Haettenschweiler", 30),foreground="#353535")
e1.grid(row= 0, column = 0,columnspan=6)
e1.config(state="disabled")

def enter(event):
    event.widget.config(bg="#eee1c4")

def enter2(event):
    event.widget.config(bg="#065d60")

def enter3(event):
    event.widget.config(bg="#43d6bb")

def enter4(event):
    event.widget.config(bg="#86bfc6")

def leave(event):
    event.widget.config(bg='#F5EEDD')

def leave2(event):
    event.widget.config(bg='#077A7D')

def leave3(event):
    event.widget.config(bg='#7AE2CF')

def leave4(event):
    event.widget.config(bg='#9ACBD0')

def clear():
    e1.config(state="normal")
    e1.delete("1.0", tk.END)
    e1.config(state="disabled")
    numlist.clear()

def press(num):
    e1.config(state="normal")
    e1.insert(tk.END,num)
    e1.config(state="disabled")
    numlist.append(num)
    return int(num)


button_settings = {
    "background": '#F5EEDD',
    "font": ("Haettenschweiler", 30),
    "width": 7,
    "height": 3,
    "fg": "#434343",
    "activebackground": "#ADACAC",
    "activeforeground": "#3F3F3F",
    "bd" : 0
}

button_settings2 = {
    "background": '#9ACBD0',
    "font": ("Haettenschweiler", 30),
    "width": 7,
    "height": 3,
    "fg": "#434343",
    "activebackground": "#8FBADD",
    "activeforeground": "#3F3F3F",
    "bd" : 0
}

button_settings3 = {
    "background": '#7AE2CF',
    "font": ("Haettenschweiler", 30),
    "width": 12,
    "height": 3,
    "fg": "#434343",
    "activebackground": "#8FBADD",
    "activeforeground": "#3F3F3F",
    "bd" : 0,
}

button_settings4 = {
    "background": '#077A7D',
    "font": ("Haettenschweiler", 30),
    "width": 7,
    "height": 3,
    "fg": "#434343",
    "activebackground": "#8FBADD",
    "activeforeground": "#3F3F3F",
    "bd" : 0
}

def numbersaver():
    d = "".join(map(str, numlist))
    if "." in d or "pi" in d:
        return float(d)
    else:
        return int(d)


def plus():
    equal()
    global Symbol,a4
    a4 = numbersaver()
    Symbol = "+"
    clear()

def minus():
    equal()
    global Symbol,a3
    a3 = numbersaver()
    Symbol = "-"
    clear()

def multiply():
    equal()
    global Symbol,a2
    a2 = numbersaver()
    Symbol = "*"
    clear()

def divition():
    equal()
    global Symbol,a1
    a1 = numbersaver()
    Symbol = "/"
    clear()

def fact():
    num = numbersaver()
    result = 1
    for i in range(1,num+1):
        result *= i

    result = str(result)
    e1.config(state="normal")
    e1.delete("1.0", tk.END)
    e1.insert("end", result)
    e1.config(state="disabled")



def sroot():
    num = numbersaver()
    a = num**(1/2)
    a5 = str(a)
    e1.config(state="normal")
    e1.delete("1.0", tk.END)
    e1.insert("end", a5)
    e1.config(state="disabled")

def pi():
    numlist.clear()
    e1.config(state="normal")
    e1.delete("1.0", tk.END)
    e1.insert("end", str(math.pi))
    e1.config(state="disabled")
    numlist.append(math.pi)
    numbersaver()

def sin():
    num = numbersaver()
    num2 = math.radians(num)
    e1.config(state="normal")
    e1.delete("1.0", tk.END)
    e1.insert("end", str(math.sin(num2)))
    e1.config(state="disabled")

def cot():
    num = numbersaver()
    num2 = math.radians(num)
    e1.config(state="normal")
    e1.delete("1.0", tk.END)
    e1.insert("end", str(1 / math.tan(num2)))
    e1.config(state="disabled")

def cos():
    num = numbersaver()
    num2 = math.radians(num)
    e1.config(state="normal")
    e1.delete("1.0", tk.END)
    e1.insert("end", str(math.cos(num2)))
    e1.config(state="disabled")

def tan():
    num = numbersaver()
    num2 = math.radians(num)
    e1.config(state="normal")
    e1.delete("1.0", tk.END)
    e1.insert("end", str(math.tan(num2)))
    e1.config(state="disabled")

def power():
    equal()
    global Symbol,a5
    a5 = numbersaver()
    Symbol = "**"
    clear()
    return a5
def equal():
    global Symbol,a4,a3,a2,a1,a5
    num4 = a4
    num3 = a3
    num2 = a2
    num1 = a1
    num5 = numbersaver()
    num6 = a5
    e1.config(state="normal")
    if Symbol == "+":
        f1 = str(num4 + num5)
        e1.delete("1.0" , tk.END)
        e1.insert("end", f1)
        numlist.clear()
        numlist.append(f1)
    elif Symbol == "-":
        f2 = str(num3 - num5)
        e1.delete("1.0" , tk.END)
        e1.insert("end", f2)
        numlist.clear()
        numlist.append(f2)
    elif Symbol == "*":
        f3 = str(num2 * num5)
        e1.delete("1.0" , tk.END)
        e1.insert("end", f3)
        numlist.clear()
        numlist.append(f3)
    elif Symbol == "/":
        f4 = str(num1 / num5)
        e1.delete("1.0" , tk.END)
        e1.insert("end", f4)
        numlist.clear()
        numlist.append(f4)
    elif Symbol == "**":
        f5 = str(num6 ** num5)
        e1.delete("1.0" , tk.END)
        e1.insert("end", f5)
        numlist.clear()
        numlist.append(f5)
    e1.config(state="disabled")
    Symbol = ""
    numbersaver()

buttons = [

    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2),
    ("0",4,1)
]
B1 = tk.Button(root, text="=",**button_settings2,bg="#9ACBD0",command=equal )
B1.grid(row = 4,column = 3)
B1.bind("<Enter>", enter4)
B1.bind("<Leave>", leave4)
B2 = tk.Button(root, text="C",**button_settings,command=clear )
B2.grid(row = 4,column = 0)
B2.bind("<Enter>", enter)
B2.bind("<Leave>", leave)
B3 = tk.Button(root, text="+",**button_settings,command=plus )
B3.grid(row = 1,column = 3)
B3.bind("<Enter>", enter)
B3.bind("<Leave>", leave)
B4 = tk.Button(root, text="–",**button_settings,command=minus )
B4.grid(row = 2,column = 3)
B4.bind("<Enter>", enter)
B4.bind("<Leave>", leave)
B5 = tk.Button(root, text="×",**button_settings,command=multiply )
B5.grid(row = 3,column = 3)
B5.bind("<Enter>", enter)
B5.bind("<Leave>", leave)
B6 = tk.Button(root, text="÷",**button_settings,command=divition )
B6.grid(row = 4,column = 2)
B6.bind("<Enter>", enter)
B6.bind("<Leave>", leave)
B6 = tk.Button(root, text="√",**button_settings4,command=sroot )
B6.grid(row = 3,column = 4)
B6.bind("<Enter>", enter2)
B6.bind("<Leave>", leave2)
B6 = tk.Button(root, text="!n",**button_settings4,command=fact )
B6.grid(row = 1,column = 4)
B6.bind("<Enter>", enter2)
B6.bind("<Leave>", leave2)
B6 = tk.Button(root, text="^",**button_settings4,command=power )
B6.grid(row = 2,column = 4)
B6.bind("<Enter>", enter2)
B6.bind("<Leave>", leave2)
B6 = tk.Button(root, text="π",**button_settings4,command=pi )
B6.grid(row = 4,column = 4)
B6.bind("<Enter>", enter2)
B6.bind("<Leave>", leave2)
B6 = tk.Button(root, text="sin",**button_settings3,command=sin )
B6.grid(row = 1,column = 5)
B6.bind("<Enter>", enter3)
B6.bind("<Leave>", leave3)
B6 = tk.Button(root, text="cos",**button_settings3,command=cos )
B6.grid(row = 2,column = 5)
B6.bind("<Enter>", enter3)
B6.bind("<Leave>", leave3)
B6 = tk.Button(root, text="tan",**button_settings3,command=tan )
B6.grid(row = 3,column = 5)
B6.bind("<Enter>", enter3)
B6.bind("<Leave>", leave3)
B6 = tk.Button(root, text="cot",**button_settings3,command=cot )
B6.grid(row = 4,column = 5)
B6.bind("<Enter>", enter3)
B6.bind("<Leave>", leave3)
for text,row,col in buttons:
    B = tk.Button(root, text=text ,command= lambda t = text: press(t) , **button_settings)
    B.grid(row = row,column = col,pady = 4)
    B.bind("<Enter>", enter)
    B.bind("<Leave>", leave)

root.mainloop()