import tkinter as tk

from Get_Promo.index import entrypoint
from Get_Rate.index import *

root = tk.Tk()
root.title("MINI PROJECT II")
root.geometry("600x400")
input_label = tk.Label(root, text="MINI PROJECT II")
input_label.pack()

button = tk.Button(root, text="Generate Promo!", command=entrypoint)
button.pack()

button = tk.Button(root, text="Generate Rate Via Pulsa!", command=get_rate_via_pulsa)
button.pack()

button = tk.Button(root, text="Generate Rate By Pulsa!", command=get_rate_by_pulsa)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

if __name__ == '__main__':
    root.mainloop()
