from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from urllib.parse import urlparse
from json import loads

def preencher_formulario(browser,nome= 'Jonathas', email='dudu@du.edu',senha= '123456789', telefone='987654321'):
    """Preenche o melhor formulário"""
    browser.find_element(By.NAME, 'nome').send_keys(nome)
    browser.find_element(By.NAME, 'email').send_keys(email) 
    browser.find_element(By.NAME, 'senha').send_keys(senha)
    browser.find_element(By.NAME, 'telefone').send_keys(telefone)
    browser.find_element(By.NAME, 'btn').click()


browser = Chrome()
url = "https://curso-python-selenium.netlify.app/aula_05.html"
browser.get(url)
time.sleep(1)
url_parseada = urlparse(browser.current_url)
estrutura = {
    'nome': 'Jonathas',
    'email': 'dudu@du.edu',
    'senha': '123456789',
    'telefone': '987654321'
}
preencher_formulario(browser, **estrutura)

time.sleep(1)
d = loads(browser.find_element(By.TAG_NAME, 'textarea').text.replace('\'', "\""))
assert d == estrutura