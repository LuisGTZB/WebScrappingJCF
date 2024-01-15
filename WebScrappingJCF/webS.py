from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# start browser
driver = webdriver.Brave()

while True:
    # delay for 30 minutes
    #time.sleep(1800)
    driver.get("https://jovenesconstruyendoelfuturo.stps.gob.mx/bc/avisovinc.php")
    
    # locate login form
    username = driver.find_element_by_id("usuario")
    password = driver.find_element_by_id("passe")
    captcha = driver.find_element_by_id("recaptcha-anchor")
    login_btn = driver.find_element_by_id("btn-ing")

    # enter credentials
    username.send_keys("josegbluis@hotmail.com")
    password.send_keys("U47068156o")

    # wait for captcha to appear
    wait = WebDriverWait(driver, 10)
    captcha.click()
    wait.until(EC.element_to_be_clickable((By.ID, "recaptcha-anchor")))

    # click on the captcha
    driver.find_element_by_id("recaptcha-anchor").click()

    # click login button
    login_btn.click()


