from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

browser = Chrome()
url = "https://curso-python-selenium.netlify.app/aula_04_a.html"
browser.get(url)
time.sleep(1)
lista_n_ordenada = browser.find_element(By.TAG_NAME, 'ul')
lis = lista_n_ordenada.find_elements(By.TAG_NAME, 'li')
li = lis[0].find_elements(By.TAG_NAME, 'a')

"""
1. buscamos `ul`
2. buscamos todos `li`
3. No primeiro `li`, buscamos `a` e pegamos o seu texto

ul
    li
        a
            texto
    li
        a
            texto

"""