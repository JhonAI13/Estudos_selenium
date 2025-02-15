from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

browser = Chrome()
url = "https://curso-python-selenium.netlify.app/aula_05_b.html"
browser.get(url)
time.sleep(1)

top = browser.find_element(By.CLASS_NAME, 'topico')
lin = browser.find_elements(By.CLASS_NAME, 'linguagens')

for l in lin:
    print(l.find_element(By.TAG_NAME,'p').text)
for l in lin:
    print(l.find_element(By.TAG_NAME,'h2').text)