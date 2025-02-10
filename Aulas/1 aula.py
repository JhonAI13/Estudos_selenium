from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

browser = Chrome()
url = "https://curso-python-selenium.netlify.app/aula_03.html"
browser.get(url)
time.sleep(1)
a = browser.find_element(By.TAG_NAME, "a")
meu_ps = browser.find_elements(By.TAG_NAME, "p")
time.sleep(1)
print(meu_ps[-1].text)

for ay in range(10):
    a.click()
    meu_ps = browser.find_elements(By.TAG_NAME, "p")
    print(meu_ps[-1].text)

time.sleep(600)

# Ou, alternativamente, use input para esperar uma ação do usuário:
# input("Pressione Enter para fechar o navegador...")
browser.quit()
