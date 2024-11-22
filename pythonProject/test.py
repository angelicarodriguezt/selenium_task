import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Path to chromedriver executable (specify your path here)
chromedriver_path = "C:/Users/arodr/OneDrive/Escritorio/chromedriver-win64/chromedriver-win64/chromedriver.exe"
# Initialize the WebDriver with the path to chromedriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# 1. Open jupyter in a browser
jupyter_url = "http://localhost:8888/notebooks/great_expectations_project.ipynb" # Replace with your Jupyter server URL
token = "your token"  # Replace with your Jupyter server token
full_url = f"{jupyter_url}?token={token}"
driver.get(full_url)

# Wait for page to load
time.sleep(5)

# Click on Run Menu
run_menu = driver.find_element(By.XPATH, '//*[@id="jp-MainMenu"]/ul/li[4]')
run_menu.click()

# Wait for the dropdown to appear
time.sleep(2)

# Click on Run All Cells option
run_all_button = driver.find_element(By.XPATH, '//*[@id="jp-mainmenu-run"]/ul/li[12]')
run_all_button.click()

time.sleep(5)

# Quit the driver after the execution
driver.quit()

