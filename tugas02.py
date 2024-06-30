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

alerts_confirm_button = driver.find_element(By.XPATH,"//button[@id='confirmButton']")
alerts_prompt_button = driver.find_element(By.XPATH,"//button[@id='promtButton']")

try:
    action = ActionChains(driver)
    
    alerts_click_button = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='alertButton']")))
    action.move_to_element(alerts_click_button).click()
    action.perform()
    driver.switch_to.alert.accept()
    print('Alert Accept')
    
    alerts_timer_button = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='timerAlertButton']")))
    action.move_to_element(alerts_timer_button).click()
    action.perform()
    sleep(5)
    driver.switch_to.alert.accept()
    print('Alert Timer Accept')
    
    
except TimeoutException:
    print('tidak muncul')
    
action.perform()

