from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from urllib.parse import urlparse
from pprint import pprint


def get_alter(browser, elemento):
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

def get_pergunta(browser):
    """Retorna um dicionario com links.

    Args:
        browser (browser): a instancia do navegador
        elemento (elemento): webelement[aside, main, body, ul, or]
    """
    element = browser.find_element(By.TAG_NAME,'main')
    p = element.find_elements(By.TAG_NAME,'p')
    
    return p[-1].text


browser = Chrome()
url = "https://curso-python-selenium.netlify.app/exercicio_03.html"
browser.get(url)
time.sleep(0.008)

element = browser.find_element(By.TAG_NAME,'main')
a = element.find_element(By.TAG_NAME,'a')
a.click()
time.sleep(1)

pergunta = get_pergunta(browser)
partes = pergunta.split()
numeros = [int(parte) for parte in partes if parte.isdigit()]
num1,num2 = numeros[0], numeros[1]
num = num1 * num2
d = get_alter(browser,'main')
for a, b in d.items():
    if a != num:
        browser.get(b)
        break
time.sleep(1)

d = get_alter(browser,'main')
for a, b in d.items():
    if a == browser.title:
        browser.get(b)
        break
time.sleep(1)

url_separada = urlparse(browser.current_url)
d = get_alter(browser,'main')
for a, b in d.items():
    if a == url_separada.path.replace('/', '')   :
        browser.get(b)
        break
time.sleep(1)

d = get_pergunta(browser)
if 'diabão' in d:
    browser.refresh()
print('você conseguiu!')