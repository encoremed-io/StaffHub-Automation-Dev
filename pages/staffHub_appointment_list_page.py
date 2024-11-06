import time
from selenium import webdriver
from testdata.localvariables import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import requests
from selenium.webdriver.common.action_chains import ActionChains
import json
from selenium.webdriver.common.keys import Keys
from datetime import datetime

USERNAME = username
PASSWORD = password

class ApptListPage():
    def __init__(self,driver1,wait):
        self.driver1 = driver1
        self.wait = wait

    def clickAppointmentListPage(self):
        appointment_icon = self.driver1.find_element(By.XPATH,"//i[@class='q-icon las la-calendar']")
        action = ActionChains(self.driver1)
        action.move_to_element(appointment_icon).perform()
        all_appointments_selection = self.driver1.find_element(By.XPATH,"//a[contains(text(),'All Appointments')]")
        action.move_to_element(all_appointments_selection).perform()
        all_appointments_selection.click()
        #wait until all appointment page appears
        element = WebDriverWait(self.driver1, 20).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'List of Appointments')]")))

    def createNewAppt(self):
        #click on New Appointment Button
        self.driver1.find_element(By.XPATH,"//span[contains(text(),'New Appointment')]").click()

        #wait until New Appointment popup appears
        element = WebDriverWait(self.driver1, 20).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'New Appointment')]")))

        #click on Linked Patient dropdown list and select the test patient
        self.driver1.find_element(By.XPATH,"//div[@data-em-name='SelectLinkedPatient']").click()
        patient = self.driver1.find_element(By.XPATH,"//span[@class='n-text' and contains(text(),'Ishlah Test Auto')]")
        patient.click()

        #Click on Doctor / Service dropdown list and select the test doctor
        self.driver1.find_element(By.XPATH,"//div[@data-em-name='SelectDoctorOrService']//input[@class='n-base-selection-input']").click()
        self.driver1.find_element(By.XPATH,"//span[@class='n-text'][contains(text(),'Doctors')]").click()
        self.driver1.find_element(By.XPATH,"//span[contains(text(),'ISHLAH DOCTORS')]").click()
        self.driver1.find_element(By.XPATH,"//span[contains(text(),'Jing')]").click()

        #Populate Visit Type field
        self.driver1.find_element(By.XPATH,"//div[@data-em-name='SelectVisitType']//input[@class='n-base-selection-input']").click()
        self.driver1.find_element(By.XPATH,"//div[contains(text(),'DENTAL')]").click()
        

        #Select the appointment slot of the current date for the test doctor
        actions = ActionChains(self.driver1)
        self.driver1.find_element(By.XPATH,"//div[@data-em-name='SelectAvailableTimeslot']//input[@class='n-base-selection-input']").click()
        for _ in range(2):
            actions.send_keys(Keys.ARROW_DOWN).perform()
            time.sleep(0.2)

        actions.send_keys(Keys.ENTER).perform()
        timeslot= self.driver1.find_element(By.XPATH,"//div[@data-em-name='SelectAvailableTimeslot']").text
        print("this it the timeslot chosen",timeslot)
        createbutton = self.driver1.find_element(By.XPATH,"//button[@type='submit']")
        createbutton.click()
        time.sleep(5)

        #retrieve appointment code in the appointment list
        createdapptcode = self.driver1.find_element(By.XPATH,"//tr[1]/td[2]").text
        print("this is the appointment code for the newly created appointment : ",createdapptcode)
        return createdapptcode,timeslot

        
    def verifyApptCreatedSelenium(self,timeslot):
        apptdate = self.driver1.find_element(By.XPATH,"//tr[1]/td[1]").text
        status = self.driver1.find_element(By.XPATH,"//tr[1]/td[3]").text
        patientname = self.driver1.find_element(By.XPATH,"//tr[1]/td[4]//span").text
        print("appointment date = ",apptdate)
        assert timeslot in apptdate,"created appointment not found in appt list : incorrect timeslot"
        print("timeslot matches! :",timeslot)
        assert status == 'PENDING',"created appointment not found in appt list : wrong status"
        print("status should be PENDING, status is : ",status)
        assert patientname == 'Ishlah Test Auto', "created appointment not found in appt list : wrong patient"
        print("test patient name is ",patientname)


    def verifyApptCreatedAPI(self,createdapptcode):
        #perform login using Requests
        dataLogin = {"tenantCode" : "pah",
                       "username" : USERNAME,
                       "password" : PASSWORD}
        r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/auth/login",json=dataLogin)

        #get the JSON response body
        r_response = r.json()

        #get token from JSON response
        token=r_response["result"]["token"]
        
        
        patientlistparams = {
            "tenantCode" : "pah" ,
        }
        # Set the authorization header of the request
        headers = {"Authorization" : f"Bearer {token}"}

        #using requests library, retrieve appointment list using API AND store the response
        r2 = requests.get("https://staffhub-dev.encoremed.io/api/v1/pah/staff/appointment/list", params=patientlistparams, headers=headers)
        data = r2.json()
        # accessing values from the JSON for the latest appointment
        appointmentsdata = data['result']['appointments'][0]
        print("this is the latest appointment : \n", appointmentsdata)
        # get appointment code
        apptcode = appointmentsdata['code']
        latestpatient = appointmentsdata['patient']['name']
        print("this is the appointment code of the latest appointment in appointment list : \n",apptcode)
        assert apptcode == createdapptcode, "appointment codes do not match"
        assert latestpatient == 'Ishlah Test Auto', "Latest patient is NOT the test user"
        print("Appointment codes are matching!")

    def retrieveApptID(self,createdapptcode):
        #perform login using Requests
        dataLogin = {"tenantCode" : "pah",
                       "username" : USERNAME,
                       "password" : PASSWORD}
        r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/auth/login",json=dataLogin)

        #get the JSON response body
        r_response = r.json()

        #get token from JSON response
        token=r_response["result"]["token"]
        
        
        patientlistparams = {
            "tenantCode" : "pah" ,
        }
        # Set the authorization header of the request
        headers = {"Authorization" : f"Bearer {token}"}

        #using requests library, retrieve appointment list using API AND store the response
        r2 = requests.get("https://staffhub-dev.encoremed.io/api/v1/pah/staff/appointment/list", params=patientlistparams, headers=headers)
        data = r2.json()
        # accessing values from the JSON for the latest appointment
        appointmentsdata = data['result']['appointments'][0]
        # get appointment code
        latestApptID = appointmentsdata['id']
        print("this is the appointment ID of the latest appointment in appointment list : \n",latestApptID)
        return latestApptID



        
    def createPatient(self):
        #perform login using Requests
        dataLogin = {"tenantCode" : "pah",
                       "username" : USERNAME,
                       "password" : PASSWORD}
        r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/auth/login",json=dataLogin)

        #get the JSON response body
        r_response = r.json()

        #get token from JSON response
        token=r_response["result"]["token"]
        
        patientdata = {
            "tenantCode" : "pah" ,
            "name" : "Ishlah Test Auto",
            "identityNo" : 50505050
        }

        # Set the authorization header of the request
        headers = {"Authorization" : f"Bearer {token}"}

        #using requests library, create patient data using API AND store the response
        r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/patient/create", data=patientdata, headers=headers)

        if r.status_code == 201:
            print("Patient successfully created! : \n", r.json())
        else:
            print("Request failed: \n", r.status_code, r.text)

    def retrievePatientID(self):
        #perform login using Requests
        dataLogin = {"tenantCode" : "pah",
                       "username" : USERNAME,
                       "password" : PASSWORD}
        r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/auth/login",json=dataLogin)

        #get the JSON response body
        r_response = r.json()
        #get token from JSON response
        token=r_response["result"]["token"]
        # Set the authorization header of the request
        headers = {"Authorization" : f"Bearer {token}"}
        patientlistparam = {
            'keyword' : 'ishlah',
            'tenantCode' : 'pah'
        }
        #using requests library, call patient list using API AND store the response
        resp = requests.get("https://staffhub-dev.encoremed.io/api/v1/pah/staff/patient/list", params=patientlistparam, headers=headers)
        data = resp.json()
        # accessing values from the JSON
        patient = data["result"]["patients"]
        #print("this is patient list retrieved: \n" , patient) remove comment for debugging

        #filter to only get the patient ID of the test patient created
        patientid = None
        for patients in patient:
            if patients["name"] == "Ishlah Test Auto":
                patientid = patients["id"]
                print("This is patient id of the test patient: ", patientid)
        
        return patientid
    
    def deletepatient(self,patientID):
        #perform login using Requests
        dataLogin = {"tenantCode" : "pah",
                       "username" : USERNAME,
                       "password" : PASSWORD}
        r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/auth/login",json=dataLogin)

        #get the JSON response body
        r_response = r.json()
        #get token from JSON response
        token=r_response["result"]["token"]
        # Set the authorization header of the request
        headers = {"Authorization" : f"Bearer {token}"}
        deletepatientdata = {
            'tenantCode' : 'pah',
            'patientId' : patientID
        }
        #using requests library, perform delete patient API call AND store the response
        resp = requests.delete("https://staffhub-dev.encoremed.io/api/v1/pah/staff/patient/delete", data=deletepatientdata, headers=headers)
        data = resp.json()

        #print("this is delete API response :", data)

        if resp.status_code == 200:
            print ("Test user successfully deleted!")
        else:
            print("Test user unsuccessfully deleted!")

    def cancelLatestAppt(self,apptID):
        #perform login using Requests
        dataLogin = {"tenantCode" : "pah",
                       "username" : USERNAME,
                       "password" : PASSWORD}
        r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/auth/login",json=dataLogin)

        #get the JSON response body
        r_response = r.json()
        #get token from JSON response
        token=r_response["result"]["token"]
        # Set the authorization header of the request
        headers = {"Authorization" : f"Bearer {token}"}
        cancelapptdata = {
            'appointmentId' : apptID,
            'tenantCode' : 'pah'
        }
        #using requests library, perform delete patient API call AND store the response
        resp = requests.put("https://staffhub-dev.encoremed.io/api/v1/pah/staff/appointment/cancel", data=cancelapptdata, headers=headers)
        data = resp.json()
        #print("this is API response for cancel appointment:", data)

        if resp.status_code == 200:
            print ("Appointment successfully cancelled!")
        else:
            print("Appointment unsuccessfully cancelled!")  







    


        
        
