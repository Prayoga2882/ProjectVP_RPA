import json
from tkinter import messagebox
from ..indosat.handler_1 import *


def promo_ISAT1():
    rst = ISAT1()
    save = json.dumps({
        'provider': 'indosat',
        'name': rst[0],
        'periode': rst[1],
        'term_and_condition': rst[2],
        'status': 'active'
    })
    data = json.loads(save)
    provider_value = data['provider']
    name_value = data['name']
    periode_value = data['periode']
    term_and_condition_value = data['term_and_condition']
    status_value = data['status']

    print("Provider: " + provider_value)
    print("Name: " + name_value)
    print("Periode: " + periode_value)
    print("Term and Condition: " + term_and_condition_value)
    print("Status: " + status_value)

    # TODO: Hit Dias's API
    # try:
    #     url = 'https://api.example.com/endpoint'
    #
    #     payload = {
    #         'provider': 'telkomsel',
    #         'name': name_value,
    #         'Periode': periode_value,
    #         'term_and_condition': term_and_condition_value,
    #         'status': status_value,
    #     }
    #
    #     response = requests.post(url, json=payload)
    #
    #     print('Status Code:', response.status_code)
    #     print('Response:', response.json())
    # except Exception as e:
    #     print(e)
    #     raise Exception(" Except error from gate_1")

    messagebox.showinfo("Proses Selesai", "Proses Generate Promo telah selesai.")
