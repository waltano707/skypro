import requests
import random
from classes import BasicWord

URL = "https://jsonkeeper.com/b/NCOP"


def load_word():
    resp = requests.get(URL, verify=False)
    data = resp.json()
    word_data = random.choice(data)
    word = BasicWord(word=word_data['word'], subwords=word_data['subwords'])

    return word
