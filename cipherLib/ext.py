from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Set up the Firefox driver
firefox_options = Options()
firefox_options.headless = True  # Run Firefox in headless mode
firefox_service = Service('path/to/geckodriver')  # Set path to geckodriver
driver = webdriver.Firefox(service=firefox_service, options=firefox_options)

# Open the Firefox add-ons page
driver.get("about:addons")

# Click on the gear icon to open the add-ons settings
settings_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='settings']")
settings_button.click()

# Click on the "Install Add-on From File" button
install_button = driver.find_element(By.CSS_SELECTOR, "button[data-view-id='addons://addons/extensions']")
install_button.click()

# Select the extension file to install
input_element = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
input_element.send_keys('path/to/extension/file.xpi')

# Wait for the extension to install
driver.implicitly_wait(10)  # Wait for 10 seconds

# Close the browser
driver.quit()
