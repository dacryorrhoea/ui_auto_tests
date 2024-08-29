import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

def login(driver, email, password):
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(email)
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()

    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()

    sleep(6)


def change_password(driver):
    driver.get(r'https://myaccount.google.com/signinoptions/password?continue=https://myaccount.google.com/security?utm_source%3Dsign_in_no_continue&pli=1&rapt=AEjHL4PowWaRJHIo_vvz-FUymQ5R_oB4nh4SiYLVlYGtDgqJtusEWbEwilgqXO3FMpxA9N1P2zy6q_M2AEURI8gMUO0mLZHZ4R-AEf2cx69ImiU2CBt_msE')

    sleep(4)
    driver.find_element(By.XPATH, '//*[@id="i6"]').send_keys('Damnati1')

    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="i12"]').send_keys('Damnati1')

    sleep(1)
    driver.find_element(By.XPATH, '//button[@class="UywwFc-LgbsSe UywwFc-LgbsSe-OWXEXe-dgl2Hf wMI9H"]').click()

    sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[14]/div[2]/div/div[2]/div[2]/button/span[5]').click()


def change_name(driver, first_name, last_name):
    driver.get(r'https://myaccount.google.com/profile/name/edit?continue=https://myaccount.google.com/profile/name?continue%3Dhttps://myaccount.google.com/personal-info?utm_source%253Dsign_in_no_continue%26utm_source%3Dsign_in_no_continue&pli=1&rapt=AEjHL4OtfPMobtUl9W8i28kPmGCWrhVHfZhY74iUh1UKsdWRP3HsKQbtyf9_sUdsQXohjyw_cR51GKIEQktLRE1Fv0eGqLlYC_GaqmPU9Wza9p-D1yNG_To')

    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="i7"]').clear()
    driver.find_element(By.XPATH, '//*[@id="i7"]').send_keys(first_name)
    
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="i12"]').clear()
    driver.find_element(By.XPATH, '//*[@id="i12"]').send_keys(last_name)

    sleep(1)
    driver.find_element(By.XPATH, '//button[@class="UywwFc-LgbsSe UywwFc-LgbsSe-OWXEXe-dgl2Hf wMI9H"]').click()


def get_profile(driver):
    driver.get(r'https://myaccount.google.com/recovery/email?continue=https://myaccount.google.com/email&rapt=AEjHL4Nmsvxo5ECF1zZJPegFYSYxTxIor1WoQvLMwQgtpPfktPhS-2U8Uf6M33g68AQyexO0wUG8Lfhr5vrAxIQOohQZJ2DMaCc2k4PSDD-8XlYbNKeiBlQ')
    sleep(3)
    reserv_email = driver.find_element(By.XPATH, '//*[@type="email"]').get_attribute('value')

    driver.get(r'https://myaccount.google.com/birthday?rapt=AEjHL4OxnoEkLhA1qOfFIYMtRcychg-8R5t3DVK9CqTom9bfcQtjPM8BepbBL7GMJVRPASpDSzZsMxUusDN1gNmNs7rBev7HSS-XtD7-zLMQGNuuLP6TrqE')
    sleep(2)
    day = driver.find_element(By.XPATH, '//*[@id="i6"]').get_attribute('value')
    mouth = driver.find_element(By.XPATH, '//*[@id="i8"]').text # дописать словарик для получения номера месяца, либо мб прогнать можно через дэйтайм
    year = driver.find_element(By.XPATH, '//*[@id="i14"]').get_attribute('value')

    return (reserv_email, f'{year}:{mouth}:{day}')


def save_data(email, reserv_email, first_name, last_name, date, new_password):
    df = pd.DataFrame({
        'email': [email,],
        'reserv_email': [reserv_email,],
        'first_name': [first_name,],
        'last_name': [last_name,],
        'date': [date,],
        'new_password': [new_password,],
    })
    df.to_excel('profiles.xlsx', index=True)


def logout(driver):
    driver.get('https://accounts.google.com/Logout')
    sleep(2)

# и как нибудь когда-то закинуть это всё в класс
if __name__ == '__main__':
    # ну или само собой где то это хранить и там же брать
    email = ''
    password = ''
    new_password = ''
    first_name = ''
    last_name = ''


    driver = uc.Chrome()
    driver.get('https://accounts.google.com/')

    login(driver, email, password)

    change_password(driver, new_password)
    change_name(driver, first_name, last_name)
    reserv_email, date = get_profile(driver)

    logout(driver)

    save_data(email, reserv_email, first_name, last_name, date, new_password)

    driver.quit()

