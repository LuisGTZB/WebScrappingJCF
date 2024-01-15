from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service
import pyttsx3
import winsound


# start browser
driver = webdriver.Edge()

# open website
driver.get("https://jovenesconstruyendoelfuturo.stps.gob.mx/bc/avisovinc.php")
    
# locate login form
username = driver.find_element("id","usuario")
password = driver.find_element("id","passe")
#captcha = driver.find_element_by_id("recaptcha-anchor")
login_btn = driver.find_element("id","btn-ing")

# enter credentials
username.send_keys("example@hotmail.com")
password.send_keys("*******")

# wait for captcha to appear
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "g-recaptcha")))

# click on the captcha
driver.find_element(By.CLASS_NAME, "g-recaptcha").click()

# click login button
login_btn.click()

time.sleep(60)

#get the page source after login
html_source = driver.page_source

# parse the page source with BeautifulSoup
soup = BeautifulSoup(html_source, 'html.parser')

# get the body of the webpage
body = soup.find("body")
print(body)

time.sleep(30)

while True:
    #get the page source after login
    html_source = driver.page_source

    # parse the page source with BeautifulSoup
    new_soup = BeautifulSoup(html_source, 'html.parser')

    # get the body of the webpage
    new_body = new_soup.find("body")

    if new_body != body:
        print("The body of the webpage has changed!")
        print(new_body)
        engine = pyttsx3.init()
        engine.say("Alarm!")
        engine.runAndWait()

        winsound.PlaySound("AlarmSound.wav", winsound.SND_ASYNC)

    else:
        print("No Changes yet")
        engine = pyttsx3.init()
        engine.say("Alarm!")
        engine.runAndWait()

        winsound.PlaySound("AlarmSound.wav", winsound.SND_ASYNC)

    time.sleep(600)
