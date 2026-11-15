from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
driver = webdriver.Remote(
    command_executor="http://localhost:4444",
    options=options
)
try:
    driver.get("http://host.docker.internal:5000/")
    heading = driver.find_element(By.TAG_NAME, "h1")
    status = driver.find_element(By.ID, "feature-status")
    assert heading.text == "DevOps Feature Flag Application"
    assert status.text == "New Feature: ENABLED"
    driver.save_screenshot("selenium_test.png")
    print("PASS: Application opened successfully")
    print("PASS: Feature flag status verified")
    print("PASS: Screenshot saved as selenium_test.png")
finally:
    driver.quit()
