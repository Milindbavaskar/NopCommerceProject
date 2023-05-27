from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Add_Customer:
    Click_Customer_XPATH=(By.XPATH,"//a[@href='#']//p[contains(text(),'Customers')]")
    Click_Customers_XPATH=(By.XPATH,"//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    Click_ADD_New_XPATH=(By.XPATH,"//a[@class='btn btn-primary']")
    Email_XPATH=(By.XPATH,"//input[@id='Email']")
    Password_XPATH = (By.XPATH, "//input[@id='Password']")
    Firstname_XPATH = (By.XPATH, "//input[@id='FirstName']")
    Lastname_XPATH = (By.XPATH, "//input[@id='LastName']")
    Gender_M_XPATH = (By.XPATH, "//label[@for='Gender_Male']")
    Gender_F_XPATH = (By.XPATH, "//label[@for='Gender_Female']")
    Click_Save_XPATH=(By.XPATH,"//button[@name='save']")
    DOB_XPATH=(By.XPATH,"//input[@id='DateOfBirth']")
    CompanyName_XPATH=(By.XPATH,"//input[@id='Company']")
    CompanyRole_XPATH=(By.XPATH,"//div[@class='k-multiselect-wrap k-floatwrap']")
    ManagerOfVendor_XPATH=(By.XPATH,"//select[@id='VendorId'")

    def __init__(self,driver):
        self.driver=driver

    def Click_customer(self):
        self.driver.find_element(*Add_Customer.Click_Customer_XPATH).click()

    def Click_customers(self):
        self.driver.find_element(*Add_Customer.Click_Customers_XPATH).click()

    def Click_Add_new(self):
        self.driver.find_element(*Add_Customer.Click_ADD_New_XPATH).click()


    def Enter_email(self,email):
        self.driver.find_element(*Add_Customer.Email_XPATH).send_keys(email)

    def Enter_password(self,password):
        self.driver.find_element(*Add_Customer.Password_XPATH).send_keys(password)

    def Enter_firstname(self,firstname):
        self.driver.find_element(*Add_Customer.Firstname_XPATH).send_keys(firstname)

    def Enter_lastname(self,lastname):
        self.driver.find_element(*Add_Customer.Lastname_XPATH).send_keys(lastname)

    def Click_gender_M(self):
        self.driver.find_element(*Add_Customer.Gender_M_XPATH).click()

    def Click_gender_F(self):
        self.driver.find_element(*Add_Customer.Gender_F_XPATH).click()

    def Click_Save_button(self):
        self.driver.find_element(*Add_Customer.Click_Save_XPATH).click()

    def Enter_DOB(self,date):
        self.driver.find_element(*Add_Customer.DOB_XPATH).send_keys(date)

    def Enter_CompanyName(self,name):
        self.driver.find_element(*Add_Customer.CompanyName_XPATH).send_keys(name)


    # def Enter_CompanyRoles(self):
    #      # Crole=Select(self.driver.find_element(*Add_Customer.CompanyRole_XPATH).click())
    #      # Crole.select_by_index(0)
    #     #self.driver.find_element(*Add_Customer.CompanyRole_XPATH).send_keys(role)
    #      wait = WebDriverWait(self.driver, 15)
    #      try:
    #          wait.until(expected_conditions.visibility_of_element_located(self.CompanyRole_XPATH))
    #          Crole=self.driver.find_element(*Add_Customer.CompanyRole_XPATH)
    #          Crole.select_by_visible_text(Administrators)
    #      except NoSuchElementException:
    #          pass
    #
    # def Enter_ManagerOfVendor(self,vendor):
    #      Mvendor=Select(self.driver.find_element(*Add_Customer.ManagerOfVendor_XPATH))
    #      Mvendor.select_by_index(int(vendor))
         #self.driver.find_element(*Add_Customer.ManagerOfVendor_XPATH).send_keys(vendor)











