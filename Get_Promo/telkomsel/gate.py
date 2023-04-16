import json
from Get_Promo.telkomsel.handler_1 import *
from Get_Promo.telkomsel.handler_2 import *
from tkinter import messagebox


def promo_TSEL1():
    save = json.dumps({
        'provider': 'telkomsel',
        'name': name_TSEL1(),
        'periode': periode_TSEL1(),
        'term_and_condition': term_and_condition_TSEL1(),
        'status': 'active'
    })
    data = json.loads(save)
    name_value = data['name']
    periode_value = data['periode']
    term_and_condition_value = data['term_and_condition']
    status_value = data['status']

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

    messagebox.showinfo("Proses Selesai", "Proses Generate Promo Telkomsel telah selesai.")


def promo_2():
    save = json.dumps({
        'provider': 'telkomsel',
        'name': name_TSEL2(),
        'periode': periode_TSEL2(),
        'term_and_condition': term_and_condition_TSEL2(),
        'status': 'active'
    })
    data = json.loads(save)
    name_value = data['name']
    periode_value = data['periode']
    term_and_condition_value = data['term_and_condition']
    status_value = data['status']

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
