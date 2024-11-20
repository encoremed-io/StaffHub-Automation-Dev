import requests
from testdata.localvariables import *
import json
from datetime import datetime

USERNAME = username
PASSWORD = password

#Staff: Authentication API calls
def authentication_Login():
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

def authentication_Forgot_Password():
    forgotpassworddata = {
        "tenantCode" : "pah" ,
        "username" : USERNAME ,
    }

    #using requests library, create doctor using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/auth/forgot/username", data=forgotpassworddata)
    r_response = r.json()

    if r.status_code == 200:
        print("recovery code sent to staff email! : \n", r_response)

    else: 
        print("recovery code NOT sent to staff email! : \n", r.status_code, r.text)

    return r.status_code



def doctor_Create():
    token = authentication_Login()
    createdoctordata = {
            "tenantCode" : "pah" ,
            "name" : "Automation Doc Ishlah" ,
            "code" : "AUTO1" ,
            "branchIds" : "4564d4c7-650b-4be4-89ae-061c60f01159" #this is branch ID for Klang branch, PAH
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create doctor using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/doctor/create", data=createdoctordata, headers=headers)
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
    token = authentication_Login()
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
    token = authentication_Login()
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
    token = authentication_Login()
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
    token = authentication_Login()

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
    token = authentication_Login()
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
    token = authentication_Login()
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
    token = authentication_Login()
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

#Staff: Staff API

def staff_List():
    token = authentication_Login()
    stafflistparams = {
        "tenantCode" : "pah" ,
        "statuses" : {
                "ACTIVE",
                "SUSPENDED"
        }
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/pah/staff/staff/list", params=stafflistparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Staff list successfully retrieved! : \n", r_response)

    else:
        print("Staff list unsuccessfully retrieved: \n", r.status_code, r.text)


    return r.status_code


def staff_Create():
    token = authentication_Login()
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
    token = authentication_Login()
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
    token = authentication_Login()
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
    token = authentication_Login()
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

#Staff: Appointment API
def appointment_Create():
    #get current system time
    current_time = datetime.now()
    #Convert the date to ISO format
    iso_time = current_time.isoformat()

    token = authentication_Login()
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
    token = authentication_Login()
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
    token = authentication_Login()
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
    token = authentication_Login()
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

#Staff: Visit API
def visit_Create():
    token = authentication_Login()
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
    token = authentication_Login()
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
    token = authentication_Login()
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
    token = authentication_Login()
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

#Staff: Profile API
def staffProfile_View(tenantCode):
    token = authentication_Login()
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
    token = authentication_Login()
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
    token = authentication_Login()
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

#Staff: Role API

def role_Create(name):
    token = authentication_Login()
    createroledata = {
        "tenantCode" : "pah" ,
        "name" : name ,
        "permissions" : {
                "AllStaffAccess"
        }
        
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/role/create", data=createroledata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("role successfully created! : \n", r_response)
        roleid = r_response["result"]["role"]["id"]
        print("Role ID : ", roleid)

    else:
        print("Role unsuccessfully created: \n", r.status_code, r.text)


    return r.status_code,roleid

def role_View(roleid):

    token = authentication_Login()
    viewroleparams = {
        "tenantCode" : "pah" ,
        "roleId" : roleid 
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/pah/staff/role/view", params=viewroleparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("role successfully retrieved! : \n", r_response)

    else:
        print("Role unsuccessfully retrieved! : \n", r.status_code, r.text)


    return r.status_code


def role_Update(tenantCode,roleid,name):
    token = authentication_Login()
    updateroledata = {
            "tenantCode" : tenantCode ,
            "roleId" : roleid ,
            "name" : name   
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete staff using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/pah/staff/role/update", data=updateroledata, headers=headers)
    if r.status_code == 200:
            print("role successfully updated! : \n", r.json())
    else:
            print("role unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code


def role_Delete(tenantCode,roleid):
    token = authentication_Login()
    deleteroledata = {
            "tenantCode" : tenantCode ,
            "roleId" : roleid    
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete staff using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/pah/staff/role/delete", data=deleteroledata, headers=headers)
    if r.status_code == 200:
            print("role successfully deleted! : \n", r.json())
    else:
            print("role unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Bill API

def bill_Create():
    token = authentication_Login()
    createbillJSON = {
        "tenantCode" : "pah" ,
        "payer" : {
              "name" : "auto bill generate test"
        },
        "amount" : "15.00" ,     
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/pah/staff/bill/create", json=createbillJSON, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("bill successfully created! : \n", r_response)
        billId = r_response["result"]["bill"]["id"]
        print("bill ID : ", billId)

    else:
        print("Bill unsuccessfully created: \n", r.status_code, r.text)


    return r.status_code,billId
    

def bill_List():
    token = authentication_Login()
    billlistparams = {
        "tenantCode" : "pah" ,
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/pah/staff/bill/list", params=billlistparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("bill list successfully retrieved! : \n", r_response)

    else:
        print("bill list unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def bill_View(billId):
    token = authentication_Login()
    viewbillparams = {
        "tenantCode" : "pah" ,
        "billId" : billId 
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/pah/staff/bill/view", params=viewbillparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("bill successfully retrieved! : \n", r_response)

    else:
        print("bill unsuccessfully retrieved! : \n", r.status_code, r.text)


    return r.status_code

def bill_Update(tenantCode,billId,):
    token = authentication_Login()
    updatebilldata = {
            "tenantCode" : tenantCode ,
            "billId" : billId ,
            "status" : "VOIDED"   
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete staff using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/pah/staff/bill/update", data=updatebilldata, headers=headers)
    if r.status_code == 200:
            print("Bill successfully updated! : \n", r.json())
    else:
            print("Bill unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code
