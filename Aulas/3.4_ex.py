from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from urllib.parse import urlparse
import urllib
from json import loads

def preencher_formulario(browser,nome= 'Jonathas', email='dudu@du.edu',senha= '123456789', telefone='987654321'):
    """Preenche o melhor formulário"""
    browser.find_element(By.NAME, 'nome').send_keys(nome)
    browser.find_element(By.NAME, 'email').send_keys(email) 
    browser.find_element(By.NAME, 'senha').send_keys(senha)
    browser.find_element(By.NAME, 'telefone').send_keys(telefone)
    browser.find_element(By.NAME, 'btn').click()

def query_string_to_dict(query: str) -> dict:
    """
    Converte uma query string em um dicionário.

    Args:
        query (str): Query string no formato 'chave=valor&chave2=valor2&...'

    Returns:
        dict: Dicionário com as chaves e valores decodificados.
    """
    resultado = {}
    # Divide a query string em pares chave=valor
    for par in query.split('&'):
        # Divide cada par em chave e valor; o "1" limita a divisão ao primeiro '='
        chave, valor = par.split('=', 1)
        # Decodifica o valor (por exemplo, converte '%40' em '@')
        resultado[chave] = urllib.parse.unquote(valor)
    return resultado


browser = Chrome()
url = "https://curso-python-selenium.netlify.app/exercicio_04.html"
browser.get(url)
time.sleep(1)

preencher_formulario(browser)

d = loads(browser.find_element(By.TAG_NAME, 'textarea').text.replace('\'', "\""))
f = urlparse(browser.current_url).query
f = query_string_to_dict(f)
f = dict(list(f.items())[:-1])
assert d == f