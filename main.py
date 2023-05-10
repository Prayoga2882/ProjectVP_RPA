import threading
from tkinter import messagebox
from Get_Rate.index import *

# schedule.every().day.at("08:00").do(generate_promo_telkomsel)
# schedule.every().day.at("08:00").do(generate_promo_indosat)
# schedule.every().day.at("08:00").do(generate_promo_axis)
# schedule.every().day.at("08:00").do(get_promo_shopee)
# schedule.every().day.at("08:00").do(get_promo_tokopedia)  # cannot be headless
# schedule.every().day.at("08:00").do(get_rate_via_pulsa)
# schedule.every().day.at("08:00").do(get_rate_by_pulsa)
# schedule.every().day.at("08:00").do(get_rate_sukma_convert)  # cannot be headless
# schedule.every().day.at("08:00").do(get_rate_zahra_convert)
# schedule.every().day.at("08:00").do(get_rate_cv_convert)
# schedule.every().day.at("08:00").do(get_rate_tentra_pulsa)
# schedule.every().day.at("08:00").do(get_rate_conversa)
# schedule.every().day.at("08:00").do(get_rate_sulap_pulsa)
# schedule.every().day.at("08:00").do(get_rate_pake_pulsa) # cannot be headless

scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()


if __name__ == '__main__':
    generate_promo_telkomsel()
    generate_promo_indosat()
    generate_promo_axis()
    get_promo_shopee()
    get_promo_tokopedia()
    # get_rate_via_pulsa()
    # get_rate_by_pulsa()
    # get_rate_sukma_convert()
    # get_rate_zahra_convert()
    # get_rate_cv_convert()
    # get_rate_tentra_pulsa()
    # get_rate_conversa()
    # get_rate_sulap_pulsa()
    # get_rate_pake_pulsa()

    messagebox.showinfo("Info", "Done")
