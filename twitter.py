import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.action_chains import ActionChains

def login(driver, phone, password):
    sleep(4)
    driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input').send_keys(phone)
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span').click()

    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input').send_keys(password)
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span').click()

    sleep(6)


def change_password(driver, password, new_password):
    driver.get(r'https://x.com/settings/password')

    sleep(4)
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[1]/div[1]/label/div/div[2]/div/input').send_keys(password)

    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[1]/div[3]/label/div/div[2]/div/input').send_keys(new_password)

    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[1]/div[4]/label/div/div[2]/div/input').send_keys(new_password)

    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[3]/button/div/span/span').click()


def create_post(driver, text):
    driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span').click()
    sleep(3)

    # driver.find_element(By.XPATH, '').click().send_keys(text)
    autotext = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
    ActionChains(driver).move_to_element(autotext).click(autotext).send_keys(text).perform()
    sleep(5)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span'))).click()

def check_approve_email_modal(driver):
    pass

def logout(driver):
    driver.get('https://x.com/logout')
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/button[1]/div/span/span').click()
    sleep(3)


if __name__ == '__main__':
    phone = '375445725892'
    password = 'CyberPepega12431'
    new_password = 'CyberPepega12431'
    text = 'Самое главное - это то что Микаса убила Эрена'


    driver = uc.Chrome()
    driver.get('https://x.com/i/flow/login')

    login(driver, phone, password)

    # change_password(driver, password, new_password)
    create_post(driver, text)

    logout(driver)

    driver.quit()

