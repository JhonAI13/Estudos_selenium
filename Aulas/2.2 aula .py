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
url = "https://curso-python-selenium.netlify.app/aula_04_b.html"
browser.get(url)
time.sleep(0.008)

l = ['um', 'dois', 'tres', 'quatro']
for texto in l:
    find_by_text(browser, 'div', texto).click()
    time.sleep(0.008)

for texto in l:
    browser.back()
    time.sleep(1)
    
for texto in l:
    browser.forward()
    time.sleep(1)