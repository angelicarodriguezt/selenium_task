import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Path to chromedriver executable (specify your path here)
chromedriver_path = "C:/Users/angelica_rodriguez/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"  # Replace with the actual path to chromedriver

# Initialize the WebDriver with the path to chromedriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# 1. Open DataLab in a browser
datalab_url = "https://ssn.trainings.dlabanalytics.com/"
driver.get(datalab_url)

# Wait for page to load
time.sleep(5)

# Click on SSO login option
sso_button = driver.find_element(By.ID, 'social-epam-idp')
sso_button.click()
time.sleep(5)

# Click on EPAM option
epam_button = driver.find_element(By.CLASS_NAME, 'social-phrase')
epam_button.click()
time.sleep(5)

# Enter email
email_field = driver.find_element(By.ID, 'i0116')
email_field.send_keys("angelica_rodriguez@epam.com") #replace here for your email

# Enter password
password_field = driver.find_element(By.ID, 'i0116')
password_field.send_keys("your_password") #replace here for your password

# Click on Sign In button
signin_button = driver.find_element(By.ID, 'idSIButton9')
signin_button.click()
time.sleep(5)




notebook_name = "final task 05.ipynb"  # Replace with your actual notebook name
notebook_link = driver.find_element(By.PARTIAL_LINK_TEXT, notebook_name)

# Click on the notebook link
notebook_link.click()

# Wait for the notebook to load (can be adjusted if necessary)
time.sleep(5)