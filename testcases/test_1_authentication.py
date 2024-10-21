
from pages.staffHub_login_page import LoginPage
from typing import ClassVar
from selenium.webdriver import Chrome
from testdata.localvariables import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest



USERNAME = username
PASSWORD = password
USERNAMESUSPENDED = usernamesuspended
@pytest.mark.usefixtures("setup")
class TestLoginChrome():
    driver1: Chrome
    wait : ClassVar[WebDriverWait]
    
    

    def testLogin_Success(self):

        lp = LoginPage(self.driver1,self.wait)
        #insert username in username field
        lp.enterUsername(USERNAME)
        #insert password in password field
        lp.enterPassword(PASSWORD)
        #click on login button
        lp.clickLoginButton()
        #assert correct page URL
        lp.verifyURL()
        staffname = self.driver1.find_element(By.XPATH,"//div[@class='column text-right q-mr-sm']//span[@data-v-45458cdc][1]").text
        lp.verifyStaffName(staffname)


    def testLogin_No_Credentials(self):

        lp = LoginPage(self.driver1,self.wait)
         #insert username in username field
        lp.enterUsername("")
        #insert password in password field
        lp.enterPassword("")
        #click on login button
        lp.clickLoginButton()
        #assert correct username error message
        actualErrorText = self.driver1.find_element(By.XPATH,"//div[contains(text(),'Username must be alphanumeric only')]").text
        expectedErrorText = "Username must be alphanumeric only"
        assert actualErrorText == expectedErrorText, "expected error text is "+expectedErrorText+" but got "+ actualErrorText
        print ("correct error message for no credentials entered appear : ", actualErrorText)


    def testLogin_Wrong_Credentials(self):

        lp = LoginPage(self.driver1,self.wait)
         #insert WRONG username in username field
        lp.enterUsername(USERNAME+"123123")
        #insert password in password field
        lp.enterPassword(PASSWORD)
        #click on login button
        lp.clickLoginButton()
        #assert incorrect username error message
        actualErrorText = self.driver1.find_element(By.XPATH,"//div[contains(text(),'Invalid credential.')]").text
        expectedErrorText = "Invalid credential."
        assert actualErrorText == expectedErrorText, "expected error text is "+expectedErrorText+" but got "+ actualErrorText
        print ("correct wrong username error message appeared : ", actualErrorText)
        #refresh the page
        self.driver1.refresh()
        element = WebDriverWait(self.driver1, 20).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'Login to StaffHub')]")))
        #insert username in username field
        lp.enterUsername(USERNAME)
        #insert WRONG password in password field
        lp.enterPassword(PASSWORD+"123123")
        lp.clickLoginButton()
        #assert incorrect password error message
        actualErrorText = self.driver1.find_element(By.XPATH,"//div[contains(text(),'Invalid credential.')]").text
        expectedErrorText = "Invalid credential."
        assert actualErrorText == expectedErrorText, "expected error text is "+expectedErrorText+" but got "+ actualErrorText
        print ("correct wrong password error message appeared : ", actualErrorText)

    def testLogin_suspended_staff(self):

        lp = LoginPage(self.driver1,self.wait)
         #insert suspended staff username in username field
        lp.enterUsername(USERNAMESUSPENDED)
        #insert password in password field
        lp.enterPassword(PASSWORD)
        #click on login button
        lp.clickLoginButton()
        #assert incorrect username error message
        actualErrorText = self.driver1.find_element(By.XPATH,"//div[contains(text(),'Your account has been suspended, kindly contact the administrator for further assistance')]").text
        expectedErrorText = "Your account has been suspended, kindly contact the administrator for further assistance"
        assert actualErrorText == expectedErrorText, "expected error text is "+expectedErrorText+" but got "+ actualErrorText
        print ("correct suspended username error message appeared : ", actualErrorText)

    
       

        



        
        
        

        




