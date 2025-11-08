import requests

def word_result(word):

    url = f'https://freedictionaryapi.com/api/v1/entries/en/{word}'
    response = requests.get(url).json()

    word_entries = response["entries"]

    return word_entries
