import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.AddCustomerPage import Add_Customer
from PageObjects.LoginPage import loginpage
from Utilities.readProperties import Readconfig


class Test_Add_Customer:
    url = Readconfig.URL()
    email = Readconfig.Email()
    password = Readconfig.Password()

    @pytest.mark.sanity
    def test_add_cust_002(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp = loginpage(self.driver)
        time.sleep(2)
        self.lp.Enter_Username(self.email)
        self.lp.Enter_Password(self.password)
        # self.lp.Enter_Username("admin@yourstore.com")
        # self.lp.Enter_Password("admin")
        self.lp.Click_login()
        self.driver.maximize_window()
        self.ac=Add_Customer(self.driver)
        self.ac.Click_customer()
        self.ac.Click_customers()
        time.sleep(2)
        self.ac.Click_Add_new()
        self.ac.Enter_email("Mpatil@abc.com")
        self.ac.Enter_password("Test123@")
        self.ac.Enter_firstname("Manish")
        self.ac.Enter_lastname("patil")
        self.ac.Click_gender_M()

        self.ac.Enter_DOB("05/07/1998")
        self.ac.Enter_CompanyName("Kotak")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        #self.ac.Enter_CompanyRoles()
        # Crole=Select(self.driver.find_element(By.XPATH,"//div[@class='k-widget k-multiselect k-multiselect-clearable']"))
        # Crole.select_by_visible_text("Administrators")
        #self.ac.Enter_ManagerOfVendor(1)
        Mvendor = Select(self.driver.find_element(By.XPATH,"//select[@id='VendorId']"))
        Mvendor.select_by_index(1)

        self.ac.Click_Save_button()
        time.sleep(5)
        if self.driver.title=="Customers / nopCommerce administration":
           self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\NopCommerceProject\\Screenshots\\test_002.png")

           time.sleep(2)
           self.lp.Click_logout()
           assert True
        else:
            assert False
