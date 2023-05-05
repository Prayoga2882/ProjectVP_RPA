import tkinter as tk
import threading
from Get_Rate.index import *

root = tk.Tk()
root.title("VIA PULSA GLOBAL INDONESIA")
root.geometry("1100x400")

button = tk.Button(root, text="Generate Promo Telkomsel!", command=generate_promo_telkomsel, activebackground='yellow')
button.grid(row=1, column=0, padx=5, pady=5)

button = tk.Button(root, text="Generate Promo Indosat!", command=generate_promo_indosat, activebackground='yellow')
button.grid(row=1, column=1, padx=5, pady=5)

button = tk.Button(root, text="Generate Promo Axis!", command=generate_promo_axis, activebackground='yellow')
button.grid(row=1, column=2, padx=5, pady=5)

button = tk.Button(root, text="Generate Promo Shopee!", command=get_promo_shopee, activebackground='yellow')
button.grid(row=1, column=4, padx=5, pady=5)

button = tk.Button(root, text="Generate Promo Tokopedia!", command=get_promo_tokopedia, activebackground='yellow')
button.grid(row=1, column=5, padx=5, pady=5)

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
button.grid(row=2, column=5, padx=5, pady=5)

button = tk.Button(root, text="Generate Rate Pake Pulsa!", command=get_rate_pake_pulsa, activebackground='yellow')
button.grid(row=3, column=4, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=4)

schedule.every(5).minutes.do(generate_promo_telkomsel)
schedule.every(5).minutes.do(generate_promo_indosat)
schedule.every(5).minutes.do(generate_promo_axis)
schedule.every(5).minutes.do(get_promo_shopee)
schedule.every(5).minutes.do(get_rate_via_pulsa)
schedule.every(5).minutes.do(get_rate_by_pulsa)
schedule.every(5).minutes.do(get_rate_sukma_convert)
schedule.every(5).minutes.do(get_rate_zahra_convert)
schedule.every(5).minutes.do(get_rate_cv_convert)
schedule.every(5).minutes.do(get_rate_tentra_pulsa)
schedule.every(5).minutes.do(get_rate_conversa)
schedule.every(5).minutes.do(get_rate_sulap_pulsa)

scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()

root.mainloop()
