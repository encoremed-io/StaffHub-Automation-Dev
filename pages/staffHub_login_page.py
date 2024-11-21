import time

from testdata.localvariables import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from selenium import webdriver
USERNAME = username
PASSWORD = password

class LoginPage():
    
    
    def __init__(self,driver1,wait):
        self.driver1 = driver1
        self.wait = wait
        

    def enterUsername(self,username):
        username_field= self.driver1.find_element(By.XPATH, "//input[@type='text']")
        username_field.click()
        username_field.send_keys(username)

    def enterPassword(self,password):
        password_field = self.driver1.find_element(By.XPATH, "//input[@type='password']")
        password_field.click()
        password_field.send_keys(password)
    
    def clickLoginButton(self):
        self.driver1.find_element(By.XPATH , "//button[@type='submit']").click()

    def verifyURL(self):
        #assert correct page URL
        element = WebDriverWait(self.driver1, 20).until(EC.visibility_of_element_located((By.XPATH,"//img[@class='q-mr-md']")))
        current_url = self.driver1.current_url
        expected_url = 'https://staffhub-dev.encoremed.io/ttish/dashboard'
        assert current_url == expected_url, "ExpectedURL is "+expected_url+" but got "+ current_url
        print ("successfully logged in to correct page")

    def verifyAPIresponse(self,statuscode):
        API_ENDPOINT = "https://staffhub-dev.encoremed.io/api/v1/ttish/staff/auth/login"
        r = requests.post(API_ENDPOINT)
        print(r.status_code)
        assert (statuscode == r.status_code)
        print("Response status code is ",r.status_code)

    def verifyStaffName(self,staffname):
        dataLogin = {"tenantCode" : "ttish",
                       "username" : USERNAME,
                       "password" : PASSWORD}
        API_ENDPOINT = "https://staffhub-dev.encoremed.io/api/v1/ttish/staff/auth/login"
        r= requests.post(API_ENDPOINT,json=dataLogin)
        #get the JSON response body
        r_response = r.json()

        #get staff name from JSON response
        staff_name=r_response["result"]["staff"]["name"]
        print("staff name is : "+staff_name)
        print("staff name displayed is : "+staffname)

        assert staffname == staff_name,"logged in staff name do not match"
        print("staff names are matching!")




    

                
        
        

    




