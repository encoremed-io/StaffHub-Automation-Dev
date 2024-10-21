from selenium import webdriver
from testdata.localvariables import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import requests

class OverviewPage():
    def __init__(self,driver1,wait):
        self.driver1 = driver1
        self.wait = wait

    def verifyApptOverviewBtn(self):
        #assert Appointment Overview Button can be seen
        apptOverviewButton = self.driver1.find_element(By.XPATH,"//a [@href='/pah/appointment/overview']")
        if apptOverviewButton.is_displayed():
            print ("Appointment Overview Button is found")
        else:
            print ("Appointment Overview Button is not found")
        assert apptOverviewButton.is_displayed() , "Appointment Overview Button displayed assertion failed"
        print("Appointment Overview Button visibility assertion passed")
    
    def verifyVisitOverviewBtn(self):
         #assert Visit Overview button can be seen
        visitOverviewButton = self.driver1.find_element(By.XPATH,"//a [@href='/pah/visit']")
        if visitOverviewButton.is_displayed():
            print ("Visit Overview Button is found")
        else:
            print ("Visit Overview Button is not found")
        assert visitOverviewButton.is_displayed() , "visit Overview Button displayed assertion failed"
        print("Visit Overview Button visibility assertion passed")

    def verifyPatientOverviewBtn(self):
        #assert Patient button can be seen
        patientButton = self.driver1.find_element(By.XPATH, "//span[contains(text(),'Patient')]")
        if patientButton.is_displayed():
            print ("Patient Button is found")
        else:
            print ("Patient Button is not found")
        assert patientButton.is_displayed() , "Patient Button displayed assertion failed"
        print("Patient Button visibility assertion passed")

    
    def verifyDoctorBtn(self):
         #assert Patient button can be seen
        doctorButton = self.driver1.find_element(By.XPATH, "//span[contains(text(),'Doctor')]")
        if doctorButton.is_displayed():
            print ("Doctor Button is found")
        else:
            print ("Doctor Button is not found")
        assert doctorButton.is_displayed() , "Doctor Button displayed assertion failed"
        print("Doctor Button visibility assertion passed")
    
    def verifyServiceBtn(self):
        #assert Service button can be seen
        serviceButton = self.driver1.find_element(By.XPATH, "//span[contains(text(),'Service')]")
        if serviceButton.is_displayed():
            print ("Service Button is found")
        else:
            print ("Service Button is not found")
        assert serviceButton.is_displayed() , "Service Button displayed assertion failed"
        print("Service Button visibility assertion passed")    

    def apptOverviewButtonClick(self):
        #click on Appointment Overview Button
        self.driver1.find_element(By.XPATH,"//a [@href='/pah/appointment/overview']").click()
        #wait until correct page appears
        element = WebDriverWait(self.driver1, 20).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='n-switch__button']")))
        #assert clicking button redirects user to the correct page
        current_url = self.driver1.current_url
        expected_url = 'https://staffhub-dev.encoremed.io/pah/appointment/overview'
        assert current_url == expected_url , 'expected URL is '+expected_url+ 'but current URL is '+current_url
        print("Appointment Overview button CTA assertion passed")

    def visitOverviewButtonClick(self):
        #click on Appointment Overview Button
        self.driver1.find_element(By.XPATH,"//a [@href='/pah/visit']").click()
        #wait until correct page appears
        element = WebDriverWait(self.driver1, 20).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'New Visit')]")))
        #assert clicking button redirects user to the correct page
        current_url = self.driver1.current_url
        expected_url = 'https://staffhub-dev.encoremed.io/pah/visit'
        assert current_url == expected_url , 'expected URL is '+expected_url+ 'but current URL is '+current_url
        print("Visit Overview button CTA assertion passed")

    def patientButtonClick(self):
        #click on Appointment Overview Button
        self.driver1.find_element(By.XPATH,"//span[contains(text(),'Patient')]").click()
        #wait until correct page appears
        element = WebDriverWait(self.driver1, 20).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'List Of Patient')]")))
        #assert clicking button redirects user to the correct page
        current_url = self.driver1.current_url
        expected_url = 'https://staffhub-dev.encoremed.io/pah/patient/list'
        assert current_url == expected_url , 'expected URL is '+expected_url+ 'but current URL is '+current_url
        print("Patient button CTA assertion passed")

    def doctorButtonClick(self):

        #click on Appointment Overview Button
        self.driver1.find_element(By.XPATH,"//span[text()='Doctor']").click()
        #wait until correct page appears
        element = WebDriverWait(self.driver1, 20).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'New Doctor')]")))
        #assert clicking button redirects user to the correct page
        assert element.is_displayed(),"Doctor page is not displayed"
        print("Doctor button CTA assertion passed")

       
    
    def serviceButtonClick(self):
        #click on Appointment Overview Button
        self.driver1.find_element(By.XPATH,"//span[text()='Service']").click()
        #wait until correct page appears
        element = WebDriverWait(self.driver1, 20).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'New Service')]")))
        #assert clicking button redirects user to the correct page
        assert element.is_displayed(),"Service page is not displayed"
        print("Service button CTA assertion passed")

 
        

