
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Replace 'your_browser_driver_path' with the path to your browser driver executable (e.g., chromedriver, geckodriver)
driver = webdriver.Chrome(')
driver.maximize_window()

# Replace 'bluestone_website_url' with the actual URL of Bluestone's signup page
website_url = 'https://www.bluestone.com/'
driver.get(website_url)

# Wait for the signup page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'signup-form')))

# Replace 'your_name', 'your_email', and 'your_password' with the actual test data
name = 'your_name'
email = 'your_email@example.com'
password = 'your_password'

# Fill the signup form
name_input = driver.find_element_by_id('name')
name_input.send_keys(name)

email_input = driver.find_element_by_id('email')
email_input.send_keys(email)

password_input = driver.find_element_by_id('password')
password_input.send_keys(password)

# Submit the form
signup_button = driver.find_element_by_id('signup-button')
signup_button.click()

# Wait for the signup process to complete (you can adjust the wait time as per your application)
wait.until(EC.url_contains('success'))

# Verify if the signup was successful
if 'success' in driver.current_url:
    print("Signup successful!")
else:
    print("Signup failed!")

# Close the browser
driver.quit()
