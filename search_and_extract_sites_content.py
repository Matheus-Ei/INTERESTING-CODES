from googlesearch import search
import requests
from bs4 import BeautifulSoup
from goose3 import Goose

def extract_useful_content(url):
    g = Goose()
    article = g.extract(url=url)
    content = article.cleaned_text
    return content

def search_and_print(query):
    search_results = search(query, num_results=1, lang='pt-BR')  # Faz a busca no Google e retorna os 5 primeiros resultados
    for url in search_results:
        content = extract_useful_content(url)
        print(content)
        print('---')

# Exemplo de uso
query = 'qual é a capital do brasil'
search_and_print(query)
