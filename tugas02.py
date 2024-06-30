from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://demoqa.com/alerts")

try:
    action = ActionChains(driver)
    
    alerts_click_button = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='alertButton']")))
    action.move_to_element(alerts_click_button)
    action.click()
    action.perform()
    driver.switch_to.alert.accept()
    print('Alert Accept')
    
    alerts_timer_button = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='timerAlertButton']")))
    action.move_to_element(alerts_timer_button)
    action.click()
    action.perform()
    sleep(5)
    driver.switch_to.alert.accept()
    print('Alert Timer Accept')
    
    for i in range(2):
        alerts_confirm_button = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='confirmButton']")))
        action.move_to_element(alerts_confirm_button)
        action.click()
        action.perform()
        
        sleep(1)
        if(i % 2 == 0):
            driver.switch_to.alert.accept()
            message = WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH,"//span[@id='confirmResult']")))
            action.move_to_element(message)
            action.perform()
            print('You selected Ok')
        else:
            driver.switch_to.alert.dismiss()
            message = WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH,"//span[@id='confirmResult']")))
            action.move_to_element(message)
            action.perform()
            print('You selected Cancel')
        sleep(1)
    
    for x in range(2):
        alerts_prompt_button = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='promtButton']")))
        action.move_to_element(alerts_prompt_button)
        action.click()
        action.perform()
        
        sleep(1)
        if(x % 2 == 0):
            driver.switch_to.alert.dismiss()
        else:
            nama = "Hanif Razin Rahmatullah"
            driver.switch_to.alert.send_keys(nama)
            driver.switch_to.alert.accept()
            welcome_nama = WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH,"//span[@id='promptResult']")))
            action.move_to_element(welcome_nama)
            action.perform()
            print("You Input Name")
        sleep(1)
    
except TimeoutException:
    print('tidak muncul')
    
action.perform()

