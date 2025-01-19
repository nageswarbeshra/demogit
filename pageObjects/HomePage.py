from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.XPATH, "//a[text()='Shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    pwd = (By.ID, "exampleInputPassword1")
    RadioButton =(By.CSS_SELECTOR, "#inlineRadio1")
    def shopeItems(self):
        self.driver.find_element(*HomePage.shop).click()
        Checkout = CheckOutPage(self.driver)
        return Checkout

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getPwd(self):
        return self.driver.find_element(*HomePage.pwd)

    def getRadio(self):
        return self.driver.find_element(*HomePage.RadioButton)
