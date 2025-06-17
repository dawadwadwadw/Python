import tkinter as tk
from tkinter import OptionMenu
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_plot():
    a = scale_a.get()
    b = scale_b.get()
    c = scale_c.get()

    x = np.linspace(-10, 10, 400)
    opcja = variable.get()
    if opcja == "ax2 + bx + c":
        y = a * x ** 2 + b * x + c
    else:

        y = np.divide((a * x ** 2 + b * x + c), (np.sin(x)+2), where=np.sin(x) != 0)
    ax.clear()
    ax.plot(x, y, label=f'y = {a}x² + {b}x + {c}')
    ax.legend()
    ax.set_title("Wykresa paraboli")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(-500,500)
    canvas.draw()



root = tk.Tk()
root.title("Rysowanie paraboli")
root.geometry("600x600")


scale_a = tk.Scale(root, from_=-10, to=10, orient='horizontal', label='a', command=lambda x: update_plot())
scale_a.pack()

scale_b = tk.Scale(root, from_=-10, to=10, orient='horizontal', label='b', command=lambda x: update_plot())
scale_b.pack()

scale_c = tk.Scale(root, from_=-10, to=10, orient='horizontal', label='c', command=lambda x: update_plot())
scale_c.pack()

master = root

variable = tk.StringVar(master)

OPTIONS = ["ax2 + bx + c", "(ax2 + bx + c)/x"]

variable.set(OPTIONS[0])
variable.trace_add("write", lambda *args: update_plot())

menu = OptionMenu(master, variable, *OPTIONS)
menu.pack()

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

update_plot()

root.mainloop()