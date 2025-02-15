from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

def melhor_filme(browser,filme= 'WALLE', email='dudu@du.edu', telefone='(055)987654321'):
    """Preenche o melhor formulário de 2020."""
    browser.find_element(By.NAME, 'filme').send_keys(filme)
    browser.find_element(By.NAME, 'email').send_keys(email) 
    browser.find_element(By.NAME, 'telefone').send_keys(telefone)
    browser.find_element(By.NAME, 'enviar').click()


browser = Chrome()
url = "https://curso-python-selenium.netlify.app/aula_05_c.html"
browser.get(url)
time.sleep(1)
# f = browser.find_element(By.NAME, 'filme')  
# f.send_keys('WALLE')
# e = browser.find_element(By.NAME, 'email')  
# e.send_keys('dudu@du.edu')
# t = browser.find_element(By.NAME, 'telefone')  
# t.send_keys('(055)987654321')
# e = browser.find_element(By.NAME, 'enviar')
# e.click()]
melhor_filme(browser)