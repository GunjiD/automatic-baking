from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def save_local():
    file = open('savedata.txt', 'w')
    file.write(driver.execute_script('return Game.WriteSave(1)'))
    file.close()
    return

def load_local():
    file = open('savedata.txt', 'r')
    data = "Game.LoadSave('" + file.read() + "')"
    print(data)
    driver.execute_script(data)
    file.close()
    return

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get('https://orteil.dashnet.org/cookieclicker/')
time.sleep(5)
load_local()
time.sleep(5)
for i in range(10):
    driver.execute_script('Game.ClickCookie()')
save_local()  #ローカルにセーブデータを保存
time.sleep(5)
driver.quit()