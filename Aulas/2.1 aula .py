from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

def find_by_text(browser, tag, text):
    """Encontrar O elemento com texto `text`

    Args:
        browser (browser): Instancia o browser 
        tag (texto): Conteúdo que deve estar na tag
        text (tag): Tag onde está o elemento
    """
    elementos = browser.find_elements(By.TAG_NAME, tag)
    for elemento in elementos:
        if elemento.text == text:
            return elemento

def find_by_href(browser, link):
    """Encontrar O elemento `a` com o link `link`

    Args:
        browser (browser): Instancia o browser 
        link (link): link que será procurado por todos os `a`
    """  
    elementos = browser.find_elements(By.TAG_NAME, 'a')

    for elemento in elementos:
        if elemento.get_attribute('href'):
            return elemento

browser = Chrome()
url = "https://curso-python-selenium.netlify.app/aula_04_a.html"
browser.get(url)
time.sleep(1)

# elemento_ddg = find_by_text(browser, 'a', 'DuckDuckGo')
elemento_ddg = find_by_href(browser, 'ddg')