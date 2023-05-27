import time

import allure
from allure_commons.types import AttachmentType
import pytest
from Utilities.Logger import LogGenerator
from Utilities.readProperties import Readconfig
from PageObjects.LoginPage import loginpage
from selenium import webdriver


class Test_Login:
    url=Readconfig.URL()
    email=Readconfig.Email()
    password=Readconfig.Password()
    log=LogGenerator.loggen()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Valid Credentials")
    @allure.issue("ABC-123")
    @allure.title("Test Page Title")
    def test_page_title_001(self,setup):
        self.log.info("test_login_001 is started")
        self.driver=setup
        self.log.info("opening a browser")
        self.driver.get(self.url)
        self.log.info("Going to url--->" + self.url)
        if self.driver.title=="Your store. Login":
            self.log.info("page title--->" + self.driver.title)
            self.driver.save_screenshot(
                "C:\\Users\\admin\\PycharmProjects\\NopCommerceProject\\Screenshots\\test_page_title_001.png")
            self.log.info("taking sreenshots")
            assert True
            self.log.info("test_page_title_001 is passed")
            self.driver.close()
        else:
            self.driver.save_screenshot(
                "C:\\Users\\admin\\PycharmProjects\\NopCommerceProject\\Screenshots\\test_page_title_001.png")
            self.log.info("taking sreenshots")
            self.log.info("test_page_title_001 is Failed")
            assert False
        self.log.info("test_page_title_001 is completed")

    @pytest.mark.sanity
    @allure.description("This test case verfying login fucntionality of the application")
    @allure.link("https://admin-demo.nopcommerce.com")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_002(self,setup):
        self.log.info("test_login_002 is started")
        self.driver=setup
        self.log.info("opening a browser")
        self.driver.get(self.url)
        self.log.info("Going to url--->" + self.url)
        self.lp=loginpage(self.driver)
        time.sleep(2)
        # self.lp.Enter_Username("admin@yourstore.com")
        # self.lp.Enter_Password("admin")
        self.lp.Enter_Username(self.email)
        self.log.info("Entering Email--->" + self.email)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering Password--->" + self.password)
        self.lp.Click_login()
        self.log.info("clicking login")
        time.sleep(2)
        if self.driver.title == "Dashboard / nopCommerce administration":
            self.log.info("page title--->" + self.driver.title)
            self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\NopCommerceProject\\Screenshots\\test_001.png")
            self.log.info("taking sreenshots")
            self.lp.Click_logout()
            self.log.info("clicking on logout")
            assert True
            self.log.info("test_login_002 is passed")
        else:
            self.log.info("page title--->" + self.driver.title)
            self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\NopCommerceProject\\Screenshots\\test_001.png")
            self.log.info("test_login_002 is failed")
            assert False

        self.log.info("test_login_002 is completed")



