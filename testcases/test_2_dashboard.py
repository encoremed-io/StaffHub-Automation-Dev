from selenium import webdriver
from typing import ClassVar
from selenium.webdriver import Chrome
from testdata.localvariables import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.staffHub_login_page import LoginPage
from pages.staffHub_overview_page import OverviewPage
USERNAME = username
PASSWORD = password
import requests

@pytest.mark.usefixtures("setup")

class TestDashboardChrome():
    driver1: ClassVar[Chrome]
    wait : ClassVar[WebDriverWait]

    def testApptOverviewButton(self):

        #perform login
        lp = LoginPage(self.driver1,self.wait) # type: ignore
        lp.enterUsername(USERNAME)
        lp.enterPassword(PASSWORD)
        lp.clickLoginButton()
   
        

        #Verify Appointment Overview Button can be seen
        op = OverviewPage(self.driver1,self.wait)
        op.verifyApptOverviewBtn()
        
        #verify Appointment Overview Button is clickable and goes to the correct page
        op.apptOverviewButtonClick()




    def testVisitOverviewButton(self):
        
        op = OverviewPage(self.driver1,self.wait)
        #perform login
        lp = LoginPage(self.driver1,self.wait)
        lp.enterUsername(USERNAME)
        lp.enterPassword(PASSWORD)
        lp.clickLoginButton()

        #verify Visit OverView Button can be seen
        op.verifyVisitOverviewBtn()

        #verify Visit Overview button is clickable and goes to the right page
        op.visitOverviewButtonClick()

    def testPatientButton(self):

        op = OverviewPage(self.driver1,self.wait)
        #perform login
        lp = LoginPage(self.driver1,self.wait)
        lp.enterUsername(USERNAME)
        lp.enterPassword(PASSWORD)
        lp.clickLoginButton()
        
        #Verify Patient button can be seen
        op.verifyPatientOverviewBtn()

        #verify Patient button is clickable and goes to the right page
        op.patientButtonClick()

    def testDoctorButton(self):

        op = OverviewPage(self.driver1,self.wait)
        #perform login
        lp = LoginPage(self.driver1,self.wait)
        lp.enterUsername(USERNAME)
        lp.enterPassword(PASSWORD)
        lp.clickLoginButton()


        #Verify Doctor button can be seen
        op.verifyDoctorBtn()

        #verify Doctor button is clickable and goes to the right page
        op.doctorButtonClick()

    
    def testServiceButton(self):
        op = OverviewPage(self.driver1,self.wait)
        #perform login
        lp = LoginPage(self.driver1,self.wait)
        lp.enterUsername(USERNAME)
        lp.enterPassword(PASSWORD)
        lp.clickLoginButton()



        #verify Service button can be seen
        op.verifyServiceBtn()

        #verify Service button is clickabe and goes to the right page
        op.serviceButtonClick()


        







        




