"""
Pedro Tortello - 24/08/2020
IBM Behind the code marathon - Challenge #3
Retrieves data from given urls and saves into JSON files.
"""

# CAUTION on use! Does not output correctly for every url.
# Check JSON name and "author" value.

from bs4 import BeautifulSoup
from requests import get
from json import dump


def jsoner(address):
    req = get(address).text
    soup = BeautifulSoup(req, 'lxml')

    dataDict = {}
    dataDict["title"] = soup.article.find('h1').text
    dataDict["author"] = soup.h1.text
    body = soup.article.find('div', class_='mat-txt')
    body = body.find_all('p')
    dataDict["body"] = ""
    for p in body:
        dataDict["body"] += p.text + " "
    dataDict["body"] = dataDict["body"].strip()
    dataDict["type"] = "article"        # hard coded type !!
    dataDict["url"] = address
    
    # BUG: <PTO 2020-08-24 p:1>
    # Filename using author's name results conflicting JSON files.
    filename = dataDict["author"].replace(" ", "") + "_article.json"    # !!
    with open(filename, "w", encoding="utf-8") as file:
        dump(dataDict, file, indent=4, ensure_ascii=False)


# Given urls list
addresses = [
"https://olhardigital.com.br/colunistas/wagner_sanchez/post/o_futuro_cada_vez_mais_perto/78972",
"https://olhardigital.com.br/colunistas/wagner_sanchez/post/os_riscos_do_machine_learning/80584",
"https://olhardigital.com.br/ciencia-e-espaco/noticia/nova-teoria-diz-que-passado-presente-e-futuro-coexistem/97786",
"https://olhardigital.com.br/noticia/inteligencia-artificial-da-ibm-consegue-prever-cancer-de-mama/87030",
"https://olhardigital.com.br/ciencia-e-espaco/noticia/inteligencia-artificial-ajuda-a-nasa-a-projetar-novos-trajes-espaciais/102772",
"https://olhardigital.com.br/colunistas/jorge_vargas_neto/post/como_a_inteligencia_artificial_pode_mudar_o_cenario_de_oferta_de_credito/78999",
"https://olhardigital.com.br/ciencia-e-espaco/noticia/cientistas-criam-programa-poderoso-que-aprimora-deteccao-de-galaxias/100683"
]

# Main loop
for address in addresses:
    jsoner(address)
