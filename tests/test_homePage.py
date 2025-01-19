import time
import datetime

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testdata.homepageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):


    def test_HomePage(self,getData):
        current_time = datetime.datetime.now()
        starting_time = time.time()
        home = HomePage(self.driver)
        self.driver.get("https://rahulshettyacademy.com/angularpractice")
        print(self.driver.current_url)
        # id , class , Xpath , CSS, Name, Link locaters support  CSS SELECTOR(#id , .className)
        home.getName().send_keys(getData["name"])
        home.getemail().send_keys(getData["email"])
        home.getPwd().send_keys(getData["pwd"])
        home.getRadio().click()
        # Static Dropdown
        dropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        dropdown.select_by_visible_text(getData["gender"])
        self.driver.find_element(By.ID, "exampleCheck1").click()

        ## Css  >>  tagName[attribute='value']  -> "input[name='name']"
       ### # self.driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys(getData["name"])
        ## XPATH >>  "//tagName[@attribute='value']"  -> //input[@type='submit'
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        ## Class >>  By.CLASS_NAME,"value" -> By.CLASS_NAME,"alert-success"
        message = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success" in message
        self.driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(" Hello again")
        time.sleep(3)

        self.driver.refresh()
        stop_time = time.time()
        # driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
        print(f"{current_time} : {message} : {getData["Testcase_ID"]}: Execution time : {stop_time - starting_time}")
        # print(f"Total time : {stop_time - starting_time} ")
        time.sleep(3)



    @pytest.fixture(params=HomePageData.getTestData())
    def getData(self,request):
        return request.param

