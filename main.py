import threading
from Get_Rate.index import *

# schedule.every().day.at("08:00").do(do_promo)
schedule.every().day.at("08:00").do(do_rate)

scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()

