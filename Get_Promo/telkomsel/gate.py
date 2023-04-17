import json
from Get_Promo.telkomsel.handler_1 import *
from Get_Promo.telkomsel.handler_2 import *
from tkinter import messagebox


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
    endDate = "2023-04-23"
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


def promo_2():
    pass
