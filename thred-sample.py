import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def save_local():
    file = open('savedata.txt', 'w')
    file.write(driver.execute_script('return Game.WriteSave(1)'))
    file.close()
    return

def load_local():
    file = open('savedata.txt', 'r')
    data = "Game.LoadSave('" + file.read() + "')"
    driver.execute_script(data)
    file.close()
    return

def click_cookie():
    while True:
        driver.execute_script('Game.ClickCookie()')

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get('http://natto0wtr.web.fc2.com/CookieClicker/')
time.sleep(5)
load_local()
time.sleep(5)

if __name__ == "__main__":
    thread_click = threading.Thread(target=click_cookie)
    thread_save_local = threading.Timer(10,save_local)

    thread_click.start()
    thread_save_local.start()

#driver.quit()