
from pages.staffHub_login_page import LoginPage
from pages.staffHub_appointment_list_page import ApptListPage
from selenium import webdriver
from typing import ClassVar
from selenium.webdriver import Chrome
from testdata.localvariables import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


USERNAME = username
PASSWORD = password
@pytest.mark.usefixtures("setup")
class TestApptChrome():
    driver1: ClassVar[Chrome]
    wait : ClassVar[WebDriverWait]
    
    

    def testBookAppt(self):

        
        #initialize class objects
        lp = LoginPage(self.driver1,self.wait) 
        alp = ApptListPage(self.driver1,self.wait)

        #create test patient using the API, using Requests library
        alp.createPatient()
        testpatientID = alp.retrievePatientID()


        #perform login using Selenium
        lp.enterUsername(USERNAME)
        lp.enterPassword(PASSWORD)
        lp.clickLoginButton()
        try:
            #click on Appointment List page on the sidebar
            alp.clickAppointmentListPage()

            #open up New Appointment Dialog and submit
            newappointmentCode,timeslot= alp.createNewAppt()

            #verify newly created appointment appears in the appointment list
            alp.verifyApptCreatedSelenium(timeslot)

            #verify appointment is created via API
            alp.verifyApptCreatedAPI(newappointmentCode)

        #perform user delete if any exception is raised
        except Exception as Argument:
             print("exception raised. something went wrong..",Argument)
             alp.deletepatient(testpatientID)
             apptid= alp.retrieveApptID(newappointmentCode)
             alp.cancelLatestAppt(apptid)
             raise AssertionError(Argument)


        else:
            #delete test patient once everything is done (to prevent DB becoming messy)
            print("no exception raised. deleting patient data..")
            alp.deletepatient(testpatientID)
            #cancel appointment once everything is done (to make this script more flexible, can reuse)
            print("cancelling previously created appointment..")
            apptid= alp.retrieveApptID(newappointmentCode)
            alp.cancelLatestAppt(apptid)


    # def testJustDelete(self):
    #     #initialize class objects
    #     alp = ApptListPage(self.driver1,self.wait)

    #     testpatientID = alp.retrievePatientID()
    #     alp.deletepatient(testpatientID)
    


        



        
        

