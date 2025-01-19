from selenium.webdriver.chrome.service import Service
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

file_path = "C:/Users/nages/Downloads/download.xlsx"
fruit_name = "Apple"
service_obj = Service("C:/Users/nages/PycharmProjects/pythonSelenium/Resources/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.maximize_window()
driver.find_element(By.ID,"downloadButton").click()
time.sleep(4)
file_input = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
file_input.send_keys(file_path)
wait = WebDriverWait(driver, 10)
toast = (By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)")
wait.until(expected_conditions.visibility_of_element_located(toast))
print(driver.find_element(*toast).text)
price_coulmn = driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
actual_price = driver.find_element(By.XPATH,"//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-"+price_coulmn+"-undefined']").text
print(actual_price)