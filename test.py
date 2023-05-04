import re
import requests
import json


def regex_search_indosat():
    with open("./conf/search_words.json", "r") as f:
        search_words = json.load(f)

    url = "https://www.indosatooredoo.com/portal/id/pssensasi"
    response = requests.get(url)

    text = response.text.lower()

    search_regex = re.compile("|".join(search_words), re.IGNORECASE)
    result = search_regex.findall(text)

    print(result)


if __name__ == '__main__':
    regex_search_indosat()
