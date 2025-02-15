from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

browser = Chrome()
url = "https://curso-python-selenium.netlify.app/aula_05_a.html"
browser.get(url)
time.sleep(1)

div_1 = browser.find_element(By.ID, 'lisp')  
div_1 = browser.findelement(By.TAG_NAME, 'div')