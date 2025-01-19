from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    selectCountry = (By.ID,"country")
    # self.driver.find_element(By.ID, "country").send_keys("Ind")
    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)