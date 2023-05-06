import threading
from Get_Rate.index import *

schedule.every(5).minutes.do(generate_promo_telkomsel)
schedule.every(5).minutes.do(generate_promo_indosat)
schedule.every(5).minutes.do(generate_promo_axis)
schedule.every(5).minutes.do(get_promo_shopee)
schedule.every(5).minutes.do(get_promo_tokopedia)  # cannot be headless
schedule.every(5).minutes.do(get_rate_via_pulsa)
schedule.every(5).minutes.do(get_rate_by_pulsa)
schedule.every(5).minutes.do(get_rate_sukma_convert)  # cannot be headless
schedule.every(5).minutes.do(get_rate_zahra_convert)
schedule.every(5).minutes.do(get_rate_cv_convert)
schedule.every(5).minutes.do(get_rate_tentra_pulsa)
schedule.every(5).minutes.do(get_rate_conversa)
schedule.every(5).minutes.do(get_rate_sulap_pulsa)
schedule.every(5).minutes.do(get_rate_pake_pulsa)

scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()
