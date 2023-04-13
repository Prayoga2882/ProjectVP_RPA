import json
from handler import *


def gate_1():
    save = json.dumps({
        'provider': 'telkomsel',
        'name': name(),
        'periode': periode(),
        'term_and_condition': term_and_condition(),
    })
    data = json.loads(save)
    name_value = data['name']
    periode_value = data['periode']
    term_and_condition_value = data['term_and_condition']

    # TODO: hit the API Dias's here
    try:
        print("Name: " + name_value)
        print("Periode: " + periode_value)
        print("Term and Condition: " + term_and_condition_value)
    except:
        print("Error")
