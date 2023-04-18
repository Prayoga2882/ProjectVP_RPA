import json
from tkinter import messagebox
import requests
from Get_Promo.indosat.handler_1 import ISAT1


def launch_ISAT():
    rst = ISAT1()

    print("name: ", rst[0])
    print("periode: ", rst[1])
    print("term_and_condition: ", rst[2])

    # try:
    #     url = 'https://api.example.com/endpoint'
    #
    #     payload = {
    #         "name": rst[0],
    #         "tnc": rst[2],
    #         "startDate": "2023-04-16",
    #         "endDate": "2023-04-23",
    #         "isActive": 1
    #     }
    #
    #     response = requests.post(url, json=payload)
    #
    #     print('Status Code:', response.status_code)
    #     print('Response:', response.json())
    # except Exception as e:
    #     print(e)
    #     raise Exception(" Except error from gate_1")
    #
    # messagebox.showinfo("Proses Selesai", "Proses Generate Promo telah selesai.")
