from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Define driver,options and service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options,service=service)

# Open the browser and navigate to the URL
driver.get("https://demoqa.com/login")

#Locate username and password fields
username_field = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"userName")))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))

# Insert username and password
username_field.send_keys("frederickkankam7@gmail.com")
password_field.send_keys("F1R1E1d11")

# Close window
input("Press enter to close the browser")
driver.quit()