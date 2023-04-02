from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--user-data-dir=C:\\Users\\joaov\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--profile-directory=Default")
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path="chromedriver\\chromedriver", chrome_options=options)

driver.get("https://web.whatsapp.com")

if(input("Proseguir? " )):
    print("começou")

element = driver.find_elements(By.XPATH, ".//div[@class='p3_M1']")[0]
# with open("bill.txt", "r") as arquivo:
#     frase = arquivo.read()
#     element.send_keys(frase)
#     element.send_keys(Keys.ENTER)

texto = input("Digite a frase: ")
quantidade = input("Digite a quantidade: ")

for i in range(0, quantidade):
    element.send_keys(texto)
    element.send_keys(Keys.ENTER)