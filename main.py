import tkinter as tk
import schedule
from Get_Rate.index import *

# root = tk.Tk()
# root.title("VIA PULSA GLOBAL INDONESIA")
# root.geometry("600x400")
# input_label = tk.Label(root, text="MINI PROJECT II")
# input_label.pack()
#
# button = tk.Button(root, text="Generate Promo Telkomsel!", command=generate_promo_telkomsel)
# button.pack()
#
# button = tk.Button(root, text="Generate Promo Axis!", command=generate_promo_axis)
# button.pack()
#
# button = tk.Button(root, text="Generate Rate Via Pulsa!", command=get_rate_via_pulsa)
# button.pack()
#
# button = tk.Button(root, text="Generate Rate Via Pulsa!", command=get_rate_by_pulsa)
# button.pack()
#
# button = tk.Button(root, text="Generate Rate Sukma Convert!", command=get_rate_sukma_convert)
# button.pack()
#
# result_label = tk.Label(root, text="")
# result_label.pack()
#
# root.mainloop()


# scheduling steps every 1 week
schedule.every().monday.at("00:00").do(generate_promo_telkomsel)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
