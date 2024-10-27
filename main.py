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

# Locate the element dropdown and Textbox
elements  = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
elements.click()

text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "item-0")))
text_box.click()

#Locate the form fields
full_name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userEmail")))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "currentAddress")))
permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "permanentAddress")))
submit_button = driver.find_element(By.ID, "submit")

# Fill the form
full_name_field.send_keys("Frederick Kankam")
email_field.send_keys("frederickkankam7@gmail.com")
current_address_field.send_keys("Mataheko")
permanent_address_field.send_keys("Tema")
driver.execute_script("arguments[0].click();", submit_button)

# Close window
input("Press enter to close the browser")
driver.quit()