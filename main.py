from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os



class WebAutomation:
    def __init__(self):
        # Define driver, options, and service
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        current_directory = os.getcwd()
        prefs = {"download.default_directory": current_directory}
        chrome_options.add_experimental_option("prefs", prefs)
        service = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

        # Open the browser and navigate to the URL
        self.driver.get("https://demoqa.com/login")

    def login(self):
        # Locate username, password, and login button fields
        username_field = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "userName")))
        password_field = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "password")))
        login_button = self.driver.find_element(By.ID, "login")

        # Insert username, password, and click login button
        username_field.send_keys("FREDYKcode1")
        password_field.send_keys("FREDYK@code1")
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self):
        # Locate the element dropdown and Textbox
        elements = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        elements.click()

        text_box = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "item-0")))
        text_box.click()

        # Locate the form fields
        full_name_field = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "userName")))
        email_field = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "userEmail")))
        current_address_field = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "currentAddress")))
        permanent_address_field = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "permanentAddress")))
        submit_button = self.driver.find_element(By.ID, "submit")

        # Fill the form
        full_name_field.send_keys("Frederick Kankam")
        email_field.send_keys("frederickkankam7@gmail.com")
        current_address_field.send_keys("Mataheko")
        permanent_address_field.send_keys("Tema")
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download_file(self):
        # Locate the Upload and Download element and lick the download button
        upload_download = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "item-7")))
        upload_download.click()

        download_button = self.driver.find_element(By.ID, "downloadButton")
        self.driver.execute_script("arguments[0].click();", download_button)

    def close_browser(self):
        # Close window
        self.driver.quit()



if __name__ == "__main__":
    web_automation = WebAutomation()
    web_automation.login()
    web_automation.fill_form()
    web_automation.download_file()
    web_automation.close_browser()



















