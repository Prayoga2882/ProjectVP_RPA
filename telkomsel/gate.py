import json
from telkomsel.handler_1 import *
from telkomsel.handler_2 import *


def gate_1():
    save = json.dumps({
        'provider': 'telkomsel',
        'name': name_1(),
        'periode': periode_1(),
        'term_and_condition': term_and_condition_1(),
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


def gate_2():
    save = json.dumps({
        'provider': 'telkomsel',
        'name': name_2(),
        'periode': periode_2(),
        'term_and_condition': term_and_condition_2(),
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
