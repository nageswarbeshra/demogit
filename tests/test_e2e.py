import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass



class TestOne(BaseClass):
    def test_e2e2(self):
        home =  HomePage(self.driver)
        self.driver.get("https://rahulshettyacademy.com/angularpractice")
        CheckOutPage = home.shopeItems()
        addall = CheckOutPage.getCardTitles()
        for add in addall:
            add.click()
        CheckOutPage.getcardFooter().click()
        confirmCheckout = CheckOutPage.getcardCheckout()
        confirmCheckout.getCountry().send_keys("Ind")
        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()

        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        successtext = self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text

        assert "Success! Thank yo u!" in successtext
        print(successtext)
        # driver.find_element(By.XPATH,"//div[@class='suggestions']/ul/li/a").click()

        time.sleep(4)




