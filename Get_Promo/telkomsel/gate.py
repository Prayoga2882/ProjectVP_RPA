import json
from Get_Promo.telkomsel.handler_1 import *
from Get_Promo.telkomsel.handler_2 import *
from tkinter import messagebox
import threading


def launch_TSEL():
    thread1 = threading.Thread(target=promo_TSEL1)
    thread2 = threading.Thread(target=promo_TSEL2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("Semua fungsi selesai dijalankan.")
    messagebox.showinfo("Proses Selesai", "Proses Generate Promo Telkomsel telah selesai.")


def promo_TSEL1():
    save = json.dumps({
        'provider': 'telkomsel',
        'name': name_TSEL1(),
        'term_and_condition': term_and_condition_TSEL1(),
        'startDate': periode_TSEL1()[0],
        'endDate': periode_TSEL1()[1],
    })
    data = json.loads(save)
    name_value = data['name']
    startDate = data['startDate']
    endDate = data['endDate']
    tnc = data['term_and_condition']
    try:
        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "name": name_value,
            "tnc": tnc,
            "startDate": startDate,
            "endDate": endDate,
            "isActive": 1
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print(e)
        raise Exception(" Except error from gate_1")

    messagebox.showinfo("Proses Selesai", "Proses Generate Promo Telkomsel telah selesai.")


def promo_TSEL2():
    save = json.dumps({
        'provider': 'telkomsel',
        'name': name_TSEL2(),
        'term_and_condition': term_and_condition_TSEL2(),
        'startDate': periode_TSEL2()[0],
        'endDate': periode_TSEL2()[1],
    })
    data = json.loads(save)
    name_value = data['name']
    startDate = data['startDate']
    endDate = data['endDate']
    tnc = data['term_and_condition']
    isActive = 1

    try:
        url = 'https://ratepromo.vercel.app/promo'
        payload = {
            "name": name_value,
            "tnc": tnc,
            "startDate": startDate,
            "endDate": endDate,
            "isActive": isActive
        }

        response = requests.post(url, json=payload)
        requests.get('https://ratepromo.vercel.app/cek-expired-promo')
        print('Status Code:', response.status_code)
        print('Response:', response.json())
    except Exception as e:
        print(e)
        raise Exception(" Except error from gate_1")

    messagebox.showinfo("Proses Selesai", "Proses Generate Promo Telkomsel telah selesai.")


