import requests
from testdata.localvariables import *
import json
from datetime import datetime

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

def doctor_Create():
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


    return r.status_code,doctorid

def doctor_View(tenantCode:str,doctorID:str):
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

def doctor_Update(tenantCode:str,doctorID:str):
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

def doctor_Delete(tenantCode:str,doctorID:str):
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


def patient_Create():
    token = staffAuthentication()

    patientdata = {
            "tenantCode" : "pah" , 
            "name" : "Ishlah Test Auto",
            "identityNo" : 50505050
        }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}

    #using requests library, create patient data using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/patient/create", data=patientdata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
            print("Patient successfully created! : \n", r_response)
            patientId = r_response["result"]["patient"]["id"]
            patientName = r_response ["result"]["patient"]["name"]
            print("Patient ID : ", patientId)
            print("\nPatient Name : ",patientName)
    else:
            print("Patient unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code,patientId


def patient_View(tenantCode:str,patientID:str):
    token = staffAuthentication()
    viewPatientParams = {
            "tenantCode" : tenantCode ,
            "patientId" : patientID
        }
    
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve patient details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/pah/staff/patient/view", params=viewPatientParams, headers=headers)

    if r.status_code == 200:
            print("patient details successfully retrieved! : \n", r.json())
    else:
            print("patient details unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def patient_Update(tenantCode,patientID):
    token = staffAuthentication()
    updatePatientData = {
            "tenantCode" : tenantCode ,
            "patientId" : patientID,
            "title" : "hehe",
            "name" : "Ishlah Test Auto EDITED HEHEHEHEHE",
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update patient details using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/pah/staff/patient/update", data=updatePatientData, headers=headers)

    if r.status_code == 200:
            print("Patient details successfully updated! : \n", r.json())
    else:
            print("Patient details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code


def patient_Delete(tenantCode,patientID):
    token = staffAuthentication()
    deletepatientdata = {
            "tenantCode" : tenantCode ,
            "patientId" : patientID
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete patient using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/pah/staff/patient/delete", data=deletepatientdata, headers=headers)

    if r.status_code == 200:
            print("patient successfully deleted! : \n", r.json())
    else:
            print("patient unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

def staff_Create():
        token = staffAuthentication()
        createstaffbody = {
            "tenantCode" : "pah" ,
            "name" : "auto staff Ishlah" ,
            "username" : "ishlah3" ,
            "password" : PASSWORD ,
            "email" :  "ishlah@encoremed.io",
            "branchIds" : "98ddc463-9fe9-4054-a2ef-8965fd3e952c"
        }
        # Set the authorization header of the request
        headers = {"Authorization" : f"Bearer {token}"}
        #using requests library, create staff using API AND store the response
        r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/staff/create", data=createstaffbody, headers=headers)
        r_response = r.json()

        if r.status_code == 201:
            print("Staff successfully created! : \n", r_response)
            staffid = r_response["result"]["staff"]["id"]
            staffname = r_response ["result"]["staff"]["name"]
            print("staff ID : ", staffid)
            print("\nstaff name : ",staffname)
        else:
            print("Staff unsuccessfully created: \n", r.status_code, r.text)


        return r.status_code,staffid


def staff_View(tenantCode,staffID):
    token = staffAuthentication()
    viewStaffParams = {
            "tenantCode" : tenantCode ,
            "staffId" : staffID
        }
    
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve staff details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/pah/staff/staff/view", params=viewStaffParams, headers=headers)

    if r.status_code == 200:
            print("staff details successfully retrieved! : \n", r.json())
    else:
            print("staff details unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def staff_Update(tenantCode,staffID):
    token = staffAuthentication()
    updateStaffData = {
            "tenantCode" : tenantCode ,
            "staffId" : staffID,
            "email" : "ishlah@encoremed.io",
            "name" : "Auto Staff Ishlah edited",
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update patient details using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/pah/staff/staff/update", data=updateStaffData, headers=headers)

    if r.status_code == 200:
            print("Staff details successfully updated! : \n", r.json())
    else:
            print("Staff details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

def staff_Delete(tenantCode , staffID):
    token = staffAuthentication()
    deletestaffdata = {
            "tenantCode" : tenantCode ,
            "staffId" : staffID
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete staff using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/pah/staff/staff/delete", data=deletestaffdata, headers=headers)

    if r.status_code == 200:
            print("staff successfully deleted! : \n", r.json())
    else:
            print("staff unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

def appointment_Create():
    #get current system time
    current_time = datetime.now()
    #Convert the date to ISO format
    iso_time = current_time.isoformat()

    token = staffAuthentication()
    createapptjson = {
    "tenantCode" : "pah",
    "patient": {
        "name": "auto appointment creation patient"
    },
    "doctorId": "685ff9ac-7c70-46c1-b2b2-ae905951dcce",
    "startAt": iso_time
}
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/appointment/create", json=createapptjson, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("appointment successfully created! : \n", r_response)
        apptid = r_response["result"]["appointment"]["id"]
        print("Appointment ID : ", apptid)
    else:
            print("Appointment unsuccessfully created: \n", r.status_code, r.text)


    return r.status_code,apptid


def appointment_View(tenantCode,apptid):
    token = staffAuthentication()
    viewApptParams = {
            "tenantCode" : tenantCode ,
            "appointmentId" : apptid
        }
    
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve staff details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/pah/staff/appointment/view", params=viewApptParams, headers=headers)

    if r.status_code == 200:
            print("Appointment successfully retrieved! : \n", r.json())
    else:
            print("Appointment unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def appointment_Update(tenantCode,apptid):
    token = staffAuthentication()
    updateApptJSON = {
            "tenantCode" : tenantCode ,
            "appointmentId" : apptid,
            "remark" : "THIS IS FROM AUTOMATED APPOINTMENT UPDATE API",
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update patient details using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/pah/staff/appointment/update", json=updateApptJSON, headers=headers)

    if r.status_code == 200:
            print("appointment details successfully updated! : \n", r.json())
    else:
            print("appointment details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

def appointment_Delete(tenantCode,apptid):
    token = staffAuthentication()
    deleteapptdata = {
            "tenantCode" : tenantCode ,
            "appointmentId" : apptid    
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete staff using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/pah/staff/appointment/delete", data=deleteapptdata, headers=headers)

    if r.status_code == 200:
            print("appointment successfully deleted! : \n", r.json())
    else:
            print("appointment unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

def visit_Create():
    token = staffAuthentication()
    createvisitJSON = {
    "tenantCode" : "pah",
    "patient": {
        "name": "auto visit creation patient"
    },
    "doctorId": "685ff9ac-7c70-46c1-b2b2-ae905951dcce" #Doctor Bong
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/visit/create", json=createvisitJSON, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("Visit successfully created! : \n", r_response)
        visitid = r_response["result"]["visit"]["id"]
        print("visit ID : ", visitid)
    else:
            print("visit unsuccessfully created: \n", r.status_code, r.text)


    return r.status_code,visitid

def visit_View(tenantCode,visitid):
    token = staffAuthentication()
    viewvisitparams = {
            "tenantCode" : tenantCode ,
            "visitId" : visitid
        }
    
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve staff details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/pah/staff/visit/view", params=viewvisitparams, headers=headers)

    if r.status_code == 200:
            print("Visit successfully retrieved! : \n", r.json())
    else:
            print("Visit unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def visit_Update(tenantCode,visitid):
    token = staffAuthentication()
    updateVisitJSON = {
            "tenantCode" : tenantCode ,
            "visitId" : visitid,
            "remark" : "THIS IS FROM AUTOMATED VISIT UPDATE API",
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update patient details using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/pah/staff/visit/update", json=updateVisitJSON, headers=headers)

    if r.status_code == 200:
            print("visit details successfully updated! : \n", r.json())
    else:
            print("visit details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code


def visit_Delete(tenantCode,visitid):
    token = staffAuthentication()
    deletevisitdata = {
            "tenantCode" : tenantCode ,
            "visitId" : visitid    
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete staff using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/pah/staff/visit/delete", data=deletevisitdata, headers=headers)
    if r.status_code == 200:
            print("visit successfully deleted! : \n", r.json())
    else:
            print("visit unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

def staffProfile_View(tenantCode):
        token = staffAuthentication()
        profileviewparams = {
            "tenantCode" : tenantCode ,
                }
        # Set the authorization header of the request
        headers = {"Authorization" : f"Bearer {token}"}
        #using requests library, delete staff using API AND store the response
        r = requests.get("https://staffhub-dev.encoremed.io/api/v1/pah/staff/profile/view", params=profileviewparams, headers=headers)
        if r.status_code == 200:
            print("Staff Profile successfully retrieved : \n", r.json())
        else:
            print("Staff Profile unsuccessfully deleted! : \n", r.status_code, r.text)

        return r.status_code

def staffProfile_password(tenantCode):
        token = staffAuthentication()
        passwordupdatedata = {
                "tenantCode" : tenantCode,
                "password" : PASSWORD,
                "newPassword" : password2
        }
        # Set the authorization header of the request
        headers = {"Authorization" : f"Bearer {token}"}
        #using requests library, delete staff using API AND store the response
        r = requests.put("https://staffhub-dev.encoremed.io/api/v1/pah/staff/profile/password", data=passwordupdatedata, headers=headers)
        if r.status_code == 200:
                print("Staff password successfully updated! : \n", r.json())
                #revert password changes
                passwordupdatedata = {
                "password" : password2,
                "newPassword" : PASSWORD
                }
                headers = {"Authorization" : f"Bearer {token}"}
                r = requests.put("https://staffhub-dev.encoremed.io/api/v1/pah/staff/profile/password", data=passwordupdatedata, headers=headers)
                if r.status_code == 200:
                      print("reverted again")
                print("staff password reverted after success")
        else:
                print("Staff password unsuccessfully updated! : \n", r.status_code, r.text)
        
        return r.status_code
      

def staffProfile_Update(tenantCode,staffname):
        token = staffAuthentication()
        profileupdatedata = {
            "tenantCode" : tenantCode ,
            "name" : staffname
                }
        # Set the authorization header of the request
        headers = {"Authorization" : f"Bearer {token}"}
        #using requests library, delete staff using API AND store the response
        r = requests.put("https://staffhub-dev.encoremed.io/api/v1/pah/staff/profile/update", data=profileupdatedata, headers=headers)
        if r.status_code == 200:
            print("Staff Profile successfully updated! : \n", r.json())
        else:
            print("Staff Profile unsuccessfully updated! : \n", r.status_code, r.text)

        return r.status_code