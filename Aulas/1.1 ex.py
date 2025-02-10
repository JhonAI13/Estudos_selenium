from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from pprint import pprint
# {
#     'h1': {
#         'texto1': 'Boas vindas',
#         'texto2': 'Outro texto'
#     }
# }
browser = Chrome()
url = "https://curso-python-selenium.netlify.app/exercicio_01.html"
browser.get(url)

time.sleep(1)
elementos_p = browser.find_elements(By.XPATH, '//p[@atributo]')

actions = ActionChains(browser)
dic = {'h1':{}}
d = {}
for elemento in elementos_p:
    actions.move_to_element(elemento).perform()
    valor_atributo = elemento.get_attribute('atributo')
    texto_interno = elemento.text
    d[valor_atributo] = texto_interno
    dic['h1'] = d

pprint(dic)




time.sleep(60000)
browser.quit()
