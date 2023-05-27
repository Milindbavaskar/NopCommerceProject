import time
import pytest
from Utilities.Logger import LogGenerator
from Utilities.readProperties import Readconfig
from PageObjects.LoginPage import loginpage
from selenium import webdriver


class Test_Login_Params:
    url=Readconfig.URL()
    email=Readconfig.Email()
    password=Readconfig.Password()
    log=LogGenerator.loggen()

    # def test_page_title_001(self,setup):
    #     self.driver=setup
    #     self.driver.get(self.url)
    #     if self.driver.h1=="Admin area demo":
    #         assert True
    #         self.driver.close()
    #     else:
    #         assert False

    @pytest.mark.sanity
    def test_login_params_003(self,setup,getDataforLogin):
        self.log.info("test_login_params_003 is started")
        self.driver=setup
        self.log.info("opening a browser")
        self.driver.get(self.url)
        self.log.info("Going to url--->" + self.url)
        self.lp=loginpage(self.driver)
        time.sleep(2)
        # self.lp.Enter_Username("admin@yourstore.com")
        # self.lp.Enter_Password("admin")
        self.lp.Enter_Username(getDataforLogin[0])
        self.log.info("Entering Email--->" + getDataforLogin[0])
        self.lp.Enter_Password(getDataforLogin[1])
        self.log.info("Entering Password--->" + getDataforLogin[1])
        self.lp.Click_login()
        self.log.info("clicking login")
        time.sleep(2)
        statuslist=[]
        if self.driver.title == "Dashboard / nopCommerce administration":
            if getDataforLogin[2]=='Pass':
               self.log.info("page title--->" + self.driver.title)
               self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\NopCommerceProject\\Screenshots\\"
                                           "\\" + getDataforLogin[0] + getDataforLogin[0] + "test_param_pass_003.png")
               self.log.info("taking sreenshots")
               self.lp.Click_logout()
               self.log.info("clicking on logout button")
               statuslist.append('Pass')
            elif getDataforLogin[2] == "Fail":
                 self.log.info("page title--->" + self.driver.title)
                 self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\NopCommerceProject\\Screenshots\\"
                                           "\\" + getDataforLogin[0] + getDataforLogin[0] + "test_param_fail_003.png")
                 self.lp.Click_logout()
                 self.log.info("clicking on logout button")
                 statuslist.append("Fail")
        else:
            if getDataforLogin[2]=='Pass':
               self.log.info("page title--->" + self.driver.title)
               self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\NopCommerceProject\\Screenshots\\"
                                           "\\" + getDataforLogin[0] + getDataforLogin[0] + "test_param_fail_003.png")
               self.log.info("taking sreenshots")
               statuslist.append("Fail")
            elif getDataforLogin[2]=='Fail':
               self.log.info("page title--->" + self.driver.title)
               self.driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\NopCommerceProject\\Screenshots\\"
                                           "\\" + getDataforLogin[0] + getDataforLogin[0] + "test_param_pass_003.png")
               self.log.info("taking sreenshots")
               statuslist.append("Pass")

        if "Fail" not in statuslist:
            assert True
            self.log.info("test_login_Params_003 is Passed")
        else:
            assert False
            self.log.info("test_login_Params_003 is Failed")
        self.log.info("test_login_Params_003 is Completed")



