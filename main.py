from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Define driver, options, and service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)

try:
    # Open the browser and navigate to the URL
    driver.get("https://demoqa.com/login")

    # Locate username, password, and login button fields
    username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
    login_button = driver.find_element(By.ID, "login")

    # Insert username, password, and click login button
    username_field.send_keys("FREDYKcode1")
    password_field.send_keys("FREDYK@code1")
    driver.execute_script("arguments[0].click();", login_button)

    # Close window
    input("Press enter to close the browser")
finally:
    driver.quit()