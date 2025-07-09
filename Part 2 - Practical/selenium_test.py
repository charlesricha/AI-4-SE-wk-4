from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the browser
driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Valid login
driver.find_element(By.ID, "username").send_keys("user123")
driver.find_element(By.ID, "password").send_keys("correctpassword")
driver.find_element(By.ID, "login-button").click()

# Add wait or assert logic here
assert "Dashboard" in driver.title

driver.quit()
