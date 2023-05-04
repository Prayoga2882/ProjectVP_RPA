import tkinter as tk
from Get_Rate.index import *

root = tk.Tk()
root.title("VIA PULSA GLOBAL INDONESIA")
root.geometry("900x400")
input_label = tk.Label(root, text="MINI PROJECT II")
input_label.grid(row=0, columnspan=3)

button = tk.Button(root, text="Generate Promo Telkomsel!", command=generate_promo_telkomsel, activebackground='yellow')
button.grid(row=1, column=0, padx=5, pady=5)

button = tk.Button(root, text="Generate Promo Indosat!", command=generate_promo_indosat, activebackground='yellow')
button.grid(row=1, column=1, padx=5, pady=5)

button = tk.Button(root, text="Generate Promo Axis!", command=generate_promo_axis, activebackground='yellow')
button.grid(row=1, column=2, padx=5, pady=5)

button = tk.Button(root, text="Generate Promo Shopee!", command=get_promo_shopee, activebackground='yellow')
button.grid(row=1, column=4, padx=5, pady=5)

button = tk.Button(root, text="Generate Rate Via Pulsa!", command=get_rate_via_pulsa, activebackground='yellow')
button.grid(row=2, column=0, padx=5, pady=5)

button = tk.Button(root, text="Generate Rate By Pulsa!", command=get_rate_by_pulsa, activebackground='yellow')
button.grid(row=2, column=1, padx=5, pady=5)

button = tk.Button(root, text="Generate Rate Sukma Convert!", command=get_rate_sukma_convert, activebackground='yellow')
button.grid(row=2, column=2, padx=5, pady=5)

button = tk.Button(root, text="Generate Rate Zahra Convert!", command=get_rate_zahra_convert, activebackground='yellow')
button.grid(row=3, column=2, padx=5, pady=5)

button = tk.Button(root, text="Generate Rate CV Convert!", command=get_rate_cv_convert, activebackground='yellow')
button.grid(row=3, column=0, padx=5, pady=5)

button = tk.Button(root, text="Generate Rate Tentra Pulsa!", command=get_rate_tentra_pulsa, activebackground='yellow')
button.grid(row=3, column=1, padx=5, pady=5)

button = tk.Button(root, text="Generate Rate Conversa!", command=get_rate_conversa, activebackground='yellow')
button.grid(row=2, column=4, padx=5, pady=5)

button = tk.Button(root, text="Generate Rate Sulap Pulsa!", command=get_rate_sulap_pulsa, activebackground='yellow')
button.grid(row=2, column=4, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=4)

if __name__ == '__main__':
    root.mainloop()
