from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from pprint import pprint

browser = Chrome()
url = "https://curso-python-selenium.netlify.app/exercicio_02.html"
browser.get(url)


time.sleep(0.5)
a = browser.find_element(By.ID, "ancora")
meu_ps = browser.find_elements(By.TAG_NAME, "p")
valor_esperado = meu_ps[1].text.split()[-1]
valor_esperado

while True:
    a.click()
    meu_ps = browser.find_elements(By.TAG_NAME, "p")
    valor_atual = meu_ps[-1].text.split()[-1]
    if valor_esperado == valor_atual:
        break




time.sleep(600)
browser.quit()