import requests
from testdata.localvariables import *

USERNAME = username
PASSWORD = password

def staffAuthentication():
    #perform login using Requests
        dataLogin = {"tenantCode" : "pah",
                       "username" : USERNAME,
                       "password" : PASSWORD}
        r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/auth/login",json=dataLogin)

        #get the JSON response body
        r_response = r.json()

        #get token from JSON response
        token=r_response["result"]["token"]
        return token

def createDoctor():
    token = staffAuthentication()
    createdoctorbody = {
            "tenantCode" : "pah" ,
            "name" : "Automation Doc Ishlah" ,
            "code" : "AUTO1" ,
            "branchIds" : "4564d4c7-650b-4be4-89ae-061c60f01159" #this is branch ID for Klang branch, PAH
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create doctor using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/doctor/create", data=createdoctorbody, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
            print("Doctor successfully created! : \n", r_response)
            doctorid = r_response["result"]["doctor"]["id"]
            doctorname = r_response ["result"]["doctor"]["name"]
            print("Doctor ID : ", doctorid)
            print("\nDoctor Name : ",doctorname)
    else:
            print("Doctor unsuccessfully failed: \n", r.status_code, r.text)



    return r.status_code,doctorid,doctorname

def viewDoctor(doctorID:str,tenantCode:str):
    token = staffAuthentication()
    viewDoctorParams = {
            "tenantCode" : tenantCode ,
            "doctorId" : doctorID
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/pah/staff/doctor/view", params=viewDoctorParams, headers=headers)

    if r.status_code == 200:
            print("Doctor details successfully retrieved! : \n", r.json())
    else:
            print("Doctor details unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def updateDoctor(tenantCode:str,doctorID:str):
    token = staffAuthentication()
    updateDoctorData = {
            "tenantCode" : tenantCode ,
            "doctorId" : doctorID,
            "title" : "hehe",
            "name" : "test doctor auto name hehe",
            "code" : "AUTOHEHE",
            "branchIds" : "4564d4c7-650b-4be4-89ae-061c60f01159"
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update doctor using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/pah/staff/doctor/update", data=updateDoctorData, headers=headers)

    if r.status_code == 200:
            print("Doctor details successfully updated! : \n", r.json())
    else:
            print("Doctor details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

def deleteDoctor(doctorID:str,tenantCode:str):
    token = staffAuthentication()
    deletedoctordata = {
            "tenantCode" : tenantCode ,
            "doctorId" : doctorID
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete doctor using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/pah/staff/doctor/delete", data=deletedoctordata, headers=headers)

    if r.status_code == 200:
            print("Doctor successfully deleted! : \n", r.json())
    else:
            print("Doctor unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code


def createPatient():
    return

def retrievePatient():
    return

def updatePatient():
    return

def deletePatient():
    return

def createStaff():
    return

def retrieveStaff():
    return

def updateStaff():
    return

def deleteStaff():
    return

def createAppointment():
    return

def retrieveAppointment():
    return

def updateAppointment():
    return

def deleteAppointment():
    return

def createVisit():
    return

def retrieveVisit():
    return

def updateVisit():
    return

def deleteVisit():
    return