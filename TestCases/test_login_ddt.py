import time
import pytest

from Utilities import XLutils
from Utilities.Logger import LogGenerator
from Utilities.readProperties import Readconfig
from PageObjects.LoginPage import loginpage
from selenium import webdriver


class Test_Login_DDT:
    url=Readconfig.URL()
    log=LogGenerator.loggen()
    path="C:\\Users\\admin\\PycharmProjects\\NopCommerceProject\\TestData\\LoginData.xlsx"


    @pytest.mark.sanity
    def test_login_ddt_004(self,setup):
        self.log.info("test_login_ddt_004 is started")
        self.driver=setup
        self.log.info("opening a browser")
        self.driver.get(self.url)
        self.log.info("Going to url--->" + self.url)
        self.lp=loginpage(self.driver)
        self.row = XLutils.Rowcount(self.path, "Sheet1")
        print("Number of rows in sheet1 is-->" + str(self.row))
        # time.sleep(2)
        statuslist=[]
        for r in range(2,self.row+1):
            self.Email= XLutils.ReadData(self.path,"Sheet1",r,2)
            self.Password=XLutils.ReadData(self.path,"Sheet1",r,3)
            self.exp_result=XLutils.ReadData(self.path,"Sheet1",r,4)
            self.lp.Enter_Username(self.Email)
            self.log.info("Entering Email--->" + self.Email)
            self.lp.Enter_Password(self.Password)
            self.log.info("Entering Password--->" + self.Password)
            self.lp.Click_login()
            self.log.info("clicking login")
            time.sleep(2)
            if self.driver.title == "Dashboard / nopCommerce administration":
                if self.exp_result == 'Pass':
                    self.log.info("page title--->" + self.driver.title)
                    self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\NopCommerceProject\\Screenshots\\"
                                                "\\" "test_ddt_pass_004.png")
                    self.log.info("taking sreenshots")
                    self.lp.Click_logout()
                    self.log.info("clicking on logout button")
                    statuslist.append('Pass')
                    XLutils.WriteData(self.path,"Sheet1",r,5,"Pass")
                    
                elif self.exp_result == "Fail":
                    self.log.info("page title--->" + self.driver.title)
                    self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\NopCommerceProject\\Screenshots\\"
                                                "\\" "test_ddt_fail_004.png")
                    self.lp.Click_logout()
                    self.log.info("clicking on logout button")
                    statuslist.append("Fail")
                    XLutils.WriteData(self.path, "Sheet1", r, 5, "Fail")
            else:
                if self.exp_result == 'Pass':
                    self.log.info("page title--->" + self.driver.title)
                    self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\NopCommerceProject\\Screenshots\\"
                                                "\\" + getDataforLogin[0] + getDataforLogin[0] + "test_ddt_fail_004.png")
                    self.log.info("taking sreenshots")
                    statuslist.append("Fail")
                    XLutils.WriteData(self.path, "Sheet1", r, 5, "Fail")
                elif self.exp_result == 'Fail':
                    self.log.info("page title--->" + self.driver.title)
                    self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\NopCommerceProject\\Screenshots\\"
                                                "\\" "test_ddt_pass_004.png")
                    self.log.info("taking sreenshots")
                    statuslist.append("Pass")
                    XLutils.WriteData(self.path, "Sheet1", r, 5, "Pass")

            if "Fail" not in statuslist:
                assert True
                self.log.info("test_login_ddt_004 is Passed")
            else:
                assert False
                self.log.info("test_login_Params_004 is Failed")
            self.log.info("test_login_ddt_004 is Completed")



