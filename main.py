import threading
from Get_Rate.index import *

# schedule.every().day.at("08:00").do(do_promo)
schedule.every().day.at("08:00").do(do_rate)
# schedule.every(1).minutes.do(do_rate)
# schedule.every(1).minutes.do(do_promo)

scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()

# if __name__ == '__main__':
# do_rate()
# do_promo()
