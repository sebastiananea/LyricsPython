import requests
import json
from lyrics_api import *
from collections import Counter

while True:
    print()
    print('Welcome!')
    print()

    print('Whats the name of the artist?')
    artist_name = input('>')
    print('Whats the name of the track?')
    track_name = input('>')
    print()
    api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
    
    #Call the api
    request = requests.get(api_call)
    data = request.json()
    data = data['message']['body']
    print('API Call:' + api_call)
    print()
    cancion_uno = (data['lyrics']['lyrics_body'])
    print()
    print('Search for the second one')
    print()
    print('Whats the name of the artist?')
    artist_name = input('>')
    print('Whats the name of the track?')
    track_name = input('>')
    print()
    api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key
    
    #Call the api
    request = requests.get(api_call)
    data = request.json()
    data = data['message']['body']
    print('API Call:' + api_call)
    print()
    cancion_dos = (data['lyrics']['lyrics_body'])
    print()
    break

print('Buscando palabras en comun...')
print('...')
print('...')
cancion_uno = cancion_uno.lower()
cancion_dos = cancion_dos.lower()
def palabras(cancion_uno, cancion_dos):
    palabras = cancion_uno.split()
    palabras += cancion_dos.split()
    for x in palabras:
        for palabra in lista:
            if palabra in palabras:
                palabras.remove(palabra)
    contador = Counter(palabras)
    repetida = contador.most_common(5)
    print('Las palabras mas repetidas son: ')
    for palabra in repetida:
        print(*palabra)

lista = ['and', 'el', 'no', 'si', 'que', 'la', 'para', 'ella', 'es', 'un', 'me', 'Es', 'y', '-', 'a', 'en', 'se', 'Y', 'por', 'the', 'not', 'your', 'you', 'i', 'to', 'of', 'are', 'for', 'on',]


palabras(cancion_uno, cancion_dos)
