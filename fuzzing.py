import requests
import re

#lista = []

def requestGet(response):
    global lista

    content_response = response.content.decode("utf-8")

    pattern = re.compile(r'url="/wp-plugins/[a-z0-9.-]+')
    matches = pattern.finditer(content_response)

    for match in matches:
        #Quitamos 'url="/wp-plugins/'
        a=re.sub('url="/wp-plugins',"",match.group(0))
        #Aqui pones el link al que deseas hacerle fuzzing con los plugins wp
        b = f'{"https://www.google.com/wp-content/plugins"}{a}'
        response_uri = requests.get(b)

        if(response_uri.status_code != 404):
            #lista.append(a + " --> " +str(response_uri.status_code))
            print("[+]" + a + " --> " +str(response_uri.status_code))
        

def cambiar_pagina():

    #En este ciclo cambiaremos de pagina y la pasamos por parametro a la funcion requestGet
    for i in range(1,1000):
        requestGet(requests.get(f'{"https://github.com/orgs/wp-plugins/repositories?page="}{i}'))
        #print(lista)
        print(f'{"------------Pag"}{i}---------------')
    
cambiar_pagina()
