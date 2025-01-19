from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH,"//div[@class='card-footer']/button")
    # addall = self.driver.find_elements(By.XPATH, "//div[@class='card-footer']/button")
    cardFooter = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    checkoutButton = (By.XPATH,"//button[@class='btn btn-success']")
    # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getcardFooter(self):
        return self.driver.find_element(*CheckOutPage.cardFooter)

    def getcardCheckout(self):
        self.driver.find_element(*CheckOutPage.checkoutButton).click()
        confirmCheckout = ConfirmPage(self.driver)
        return confirmCheckout