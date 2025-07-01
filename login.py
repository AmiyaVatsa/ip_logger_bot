from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

USERNAME = "<username>"
PASSWORD = "<password>"

service = Service("/home/intern/Downloads/chromedriver-linux64/chromedriver")
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("http://neverssl.com")
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.ID, "ft_un")))
    driver.find_element(By.ID, "ft_un").clear()
    driver.find_element(By.ID, "ft_un").send_keys(USERNAME)
    driver.find_element(By.ID, "ft_pd").clear()
    driver.find_element(By.ID, "ft_pd").send_keys(PASSWORD)
    driver.find_element(By.XPATH, '//input[@type="submit" and @value="Continue"]').click()
    time.sleep(3)
    #print(driver.page_source)

finally:
    driver.quit()
