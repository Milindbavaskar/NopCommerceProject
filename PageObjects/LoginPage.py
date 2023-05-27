import time

from selenium.webdriver.common.by import By


class loginpage:
    Text_UserName_XPATH = (By.XPATH, "//input[@type='email']")
    Text_Password_XPATH = (By.XPATH, "//input[@type='password']")
    Click_Login_Button_XPATH = (By.XPATH, "//button[@type='submit']")
    Click_Logout_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self,driver):
        self.driver=driver

    def Enter_Username(self,username):
        self.driver.find_element(*loginpage.Text_UserName_XPATH).clear()
        #time.sleep(2)
        self.driver.find_element(*loginpage.Text_UserName_XPATH).send_keys(username)

    def Enter_Password(self,password):
        self.driver.find_element(*loginpage.Text_Password_XPATH).clear()
        self.driver.find_element(*loginpage.Text_Password_XPATH).send_keys(password)

    def Click_login(self):
        self.driver.find_element(*loginpage.Click_Login_Button_XPATH).click()

    def Click_logout(self):
        self.driver.find_element(*loginpage.Click_Logout_XPATH).click()



