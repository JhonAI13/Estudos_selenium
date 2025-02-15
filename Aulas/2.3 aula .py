from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from urllib.parse import urlparse
from pprint import pprint


def get_link(browser, elemento):
    """Retorna um dicionario com links.

    Args:
        browser (browser): a instancia do navegador
        elemento (elemento): webelement[aside, main, body, ul, or]
    """
    element = browser.find_element(By.TAG_NAME,elemento)
    element_a = element.find_elements(By.TAG_NAME,'a')
    d = {}
    for a in element_a:
        d[a.text] = a.get_attribute('href')
    return d

browser = Chrome()
url = "https://curso-python-selenium.netlify.app/aula_04.html"
browser.get(url)
time.sleep(0.008)


url_separada = urlparse(browser.current_url)


pprint(get_link(browser,'aside'))
"""
browser.get(d['Aula 3'])
browser.get(d['Aula 4'])
"""

exercicios = get_link(browser, 'main')
pprint(exercicios)
browser.get(exercicios['Exercício 3'])
https://curso-python-selenium.netlify.app/exercicio_03.html