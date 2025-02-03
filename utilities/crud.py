import requests
from testdata.localvariables import *
import json
from datetime import datetime,timezone
import pandas

USERNAME = username
PASSWORD = password
tenantCode = 'ttish'
#Staff: Authentication API calls
def authentication_Login():
    #perform login using Requests
        dataLogin = {"tenantCode" : tenantCode,
                       "username" : USERNAME,
                       "password" : PASSWORD}
        r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/auth/login",json=dataLogin)

        #get the JSON response body
        r_response = r.json()

        #get token from JSON response
        token=r_response["result"]["token"]
        return token

def authentication_Forgot_Password():
    forgotpassworddata = {
        "tenantCode" : tenantCode ,
        "username" : USERNAME ,
    }

    #using requests library, create doctor using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/auth/forgot/username", data=forgotpassworddata)
    r_response = r.json()

    if r.status_code == 200:
        print("recovery code sent to staff email! : \n", r_response)

    else: 
        print("recovery code NOT sent to staff email! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Doctor API

def doctor_Create():
    token = authentication_Login()
    createdoctordata = {
            "tenantCode" : tenantCode ,
            "name" : "Automation Doc Ishlah" ,
            "code" : "AUTO1" ,
            "branchIds" : "5608b972-2f93-4330-a2e8-83bad4c9fa84"
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create doctor using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/doctor/create", data=createdoctordata, headers=headers)
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

def doctor_View(doctorID:str):
    token = authentication_Login()
    viewDoctorParams = {
            "tenantCode" : tenantCode ,
            "doctorId" : doctorID
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/doctor/view", params=viewDoctorParams, headers=headers)

    if r.status_code == 200:
            print("Doctor details successfully retrieved! : \n", r.json())
    else:
            print("Doctor details unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def doctor_Update(doctorID:str):
    token = authentication_Login()
    updateDoctorData = {
            "tenantCode" : tenantCode ,
            "doctorId" : doctorID,
            "title" : "hehe",
            "name" : "test doctor auto name hehe",
            "code" : "AUTOHEHE",
            "branchIds" : "5608b972-2f93-4330-a2e8-83bad4c9fa84"
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update doctor using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/doctor/update", data=updateDoctorData, headers=headers)

    if r.status_code == 200:
            print("Doctor details successfully updated! : \n", r.json())
    else:
            print("Doctor details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

def doctor_Delete(doctorID:str):
    token = authentication_Login()
    deletedoctordata = {
            "tenantCode" : tenantCode ,
            "doctorId" : doctorID
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete doctor using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/doctor/delete", data=deletedoctordata, headers=headers)

    if r.status_code == 200:
            print("Doctor successfully deleted! : \n", r.json())
    else:
            print("Doctor unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code


def patient_Create(patientName,identityNo):
    token = authentication_Login()

    patientdata = {
            "tenantCode" : tenantCode , 
            "name" : patientName,
            "identityNo" : identityNo
        }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}

    #using requests library, create patient data using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/patient/create", data=patientdata, headers=headers)
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


def patient_View(patientID:str):
    token = authentication_Login()
    viewPatientParams = {
            "tenantCode" : tenantCode ,
            "patientId" : patientID
        }
    
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve patient details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/patient/view", params=viewPatientParams, headers=headers)

    if r.status_code == 200:
            print("patient details successfully retrieved! : \n", r.json())
    else:
            print("patient details unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def patient_Update(patientID):
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
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/patient/update", data=updatePatientData, headers=headers)

    if r.status_code == 200:
            print("Patient details successfully updated! : \n", r.json())
    else:
            print("Patient details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code


def patient_Delete(patientID):
    token = authentication_Login()
    deletepatientdata = {
            "tenantCode" : tenantCode ,
            "patientId" : patientID
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete patient using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/patient/delete", data=deletepatientdata, headers=headers)

    if r.status_code == 200:
            print("patient successfully deleted! : \n", r.json())
    else:
            print("patient unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Staff API

def staff_List():
    token = authentication_Login()
    stafflistparams = {
        "tenantCode" : tenantCode ,
        "statuses" : {
                "ACTIVE",
                "SUSPENDED"
        }
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/staff/list", params=stafflistparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Staff list successfully retrieved! : \n", r_response)

    else:
        print("Staff list unsuccessfully retrieved: \n", r.status_code, r.text)


    return r.status_code


def staff_Create():
    token = authentication_Login()
    createstaffbody = {
        "tenantCode" : tenantCode ,
        "name" : "auto staff Ishlah" ,
        "username" : username2 ,
        "password" : PASSWORD ,
        "email" :  "ishlah@encoremed.io",
        "branchIds" : "98ddc463-9fe9-4054-a2ef-8965fd3e952c"
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/staff/create", data=createstaffbody, headers=headers)
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


def staff_View(staffID):
    token = authentication_Login()
    viewStaffParams = {
            "tenantCode" : tenantCode ,
            "staffId" : staffID
        }
    
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve staff details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/staff/view", params=viewStaffParams, headers=headers)

    if r.status_code == 200:
            print("staff details successfully retrieved! : \n", r.json())
    else:
            print("staff details unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def staff_Update(staffID):
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
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/staff/update", data=updateStaffData, headers=headers)

    if r.status_code == 200:
            print("Staff details successfully updated! : \n", r.json())
    else:
            print("Staff details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

def staff_Delete( staffID):
    token = authentication_Login()
    deletestaffdata = {
            "tenantCode" : tenantCode ,
            "staffId" : staffID
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete staff using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/staff/delete", data=deletestaffdata, headers=headers)

    if r.status_code == 200:
            print("staff successfully deleted! : \n", r.json())
    else:
            print("staff unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Appointment API
def appointment_Create():
    #get current system time
    current_time = datetime.now()
    current_time_floored = pandas.Timestamp(current_time).floor('5T').to_pydatetime()
    iso_time = current_time_floored.isoformat()+'Z'

    print (iso_time)
    token = authentication_Login()
    createapptjson = {
    "tenantCode" : tenantCode,
    "patient": {
        "name": "auto appointment creation patient" 
    }, #doctor viktor
    "doctorId": "8474adad-aa86-4a8e-b0ed-918024d21f82",
    "startAt": iso_time
}
    
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/appointment/create", json=createapptjson, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("appointment successfully created! : \n", r_response)
        apptid = r_response["result"]["appointment"]["id"]
        print("Appointment ID : ", apptid)
    else:
            print("Appointment unsuccessfully created: \n", r.status_code, r.text)


    return r.status_code,apptid


def appointment_View(apptid):
    token = authentication_Login()
    viewApptParams = {
            "tenantCode" : tenantCode ,
            "appointmentId" : apptid
        }
    
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve staff details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/appointment/view", params=viewApptParams, headers=headers)

    if r.status_code == 200:
            print("Appointment successfully retrieved! : \n", r.json())
    else:
            print("Appointment unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def appointment_Update(apptid):
    token = authentication_Login()
    updateApptJSON = {
            "tenantCode" : tenantCode ,
            "appointmentId" : apptid,
            "remark" : "THIS IS FROM AUTOMATED APPOINTMENT UPDATE API",
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update patient details using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/appointment/update", json=updateApptJSON, headers=headers)

    if r.status_code == 200:
            print("appointment details successfully updated! : \n", r.json())
    else:
            print("appointment details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

def appointment_Delete(apptid):
    token = authentication_Login()
    deleteapptdata = {
            "tenantCode" : tenantCode ,
            "appointmentId" : apptid    
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete staff using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/appointment/delete", data=deleteapptdata, headers=headers)

    if r.status_code == 200:
            print("appointment successfully deleted! : \n", r.json())
    else:
            print("appointment unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Visit API
def visit_Create():
    token = authentication_Login()
    createvisitJSON = {
    "tenantCode" : tenantCode,
    "patient": {
        "name": "auto visit creation patient"
    },
    "doctorId": "8474adad-aa86-4a8e-b0ed-918024d21f82" #Doctor Viktor
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visit/create", json=createvisitJSON, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("Visit successfully created! : \n", r_response)
        visitid = r_response["result"]["visit"]["id"]
        visitpatientId=r_response["result"]["visit"]["patient"]["id"]
        print("visit ID : ", visitid)
        print("Visit patient ID : ",visitpatientId)
    else:
            print("visit unsuccessfully created: \n", r.status_code, r.text)

    
    return r.status_code,visitid,visitpatientId

def visit_View(visitid):
    token = authentication_Login()
    viewvisitparams = {
            "tenantCode" : tenantCode ,
            "visitId" : visitid
        }
    
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve staff details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visit/view", params=viewvisitparams, headers=headers)

    if r.status_code == 200:
            print("Visit successfully retrieved! : \n", r.json())
    else:
            print("Visit unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def visit_Update(visitid):
    token = authentication_Login()
    updateVisitJSON = {
            "tenantCode" : tenantCode ,
            "visitId" : visitid,
            "remark" : "THIS IS FROM AUTOMATED VISIT UPDATE API",
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update patient details using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visit/update", json=updateVisitJSON, headers=headers)

    if r.status_code == 200:
            print("visit details successfully updated! : \n", r.json())
    else:
            print("visit details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code


def visit_Delete(visitid):
    token = authentication_Login()
    deletevisitdata = {
            "tenantCode" : tenantCode ,
            "visitId" : visitid    
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete staff using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visit/delete", data=deletevisitdata, headers=headers)
    if r.status_code == 200:
            print("visit successfully deleted! : \n", r.json())
    else:
            print("visit unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Profile API
def staffProfile_View():
    token = authentication_Login()
    profileviewparams = {
        "tenantCode" : tenantCode ,
            }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete staff using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/profile/view", params=profileviewparams, headers=headers)
    if r.status_code == 200:
        print("Staff Profile successfully retrieved : \n", r.json())
    else:
        print("Staff Profile unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

def staffProfile_password():
    token = authentication_Login()
    passwordupdatedata = {
            "tenantCode" : tenantCode,
            "password" : PASSWORD,
            "newPassword" : password2
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete staff using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/profile/password", data=passwordupdatedata, headers=headers)
    if r.status_code == 200:
            print("Staff password successfully updated! : \n", r.json())
            #revert password changes
            passwordupdatedata = {
            "password" : password2,
            "newPassword" : PASSWORD
            }
            headers = {"Authorization" : f"Bearer {token}"}
            r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/profile/password", data=passwordupdatedata, headers=headers)
            if r.status_code == 200:
                    print("reverted again")
            print("staff password reverted after success")
    else:
            print("Staff password unsuccessfully updated! : \n", r.status_code, r.text)
    
    return r.status_code
      

def staffProfile_Update(staffname):
    token = authentication_Login()
    profileupdatedata = {
        "tenantCode" : tenantCode ,
        "name" : staffname
            }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete staff using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/profile/update", data=profileupdatedata, headers=headers)
    if r.status_code == 200:
        print("Staff Profile successfully updated! : \n", r.json())
    else:
        print("Staff Profile unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Role API

def role_Create(name):
    token = authentication_Login()
    createroledata = {
        "tenantCode" : tenantCode ,
        "name" : name ,
        "permissions" : {
                "AllStaffAccess"
        }
        
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/role/create", data=createroledata, headers=headers)
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
        "tenantCode" : tenantCode ,
        "roleId" : roleid 
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/role/view", params=viewroleparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("role successfully retrieved! : \n", r_response)

    else:
        print("Role unsuccessfully retrieved! : \n", r.status_code, r.text)


    return r.status_code


def role_Update(roleid,name):
    token = authentication_Login()
    updateroledata = {
            "tenantCode" : tenantCode ,
            "roleId" : roleid ,
            "name" : name   
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete staff using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/role/update", data=updateroledata, headers=headers)
    if r.status_code == 200:
            print("role successfully updated! : \n", r.json())
    else:
            print("role unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code


def role_Delete(roleid):
    token = authentication_Login()
    deleteroledata = {
            "tenantCode" : tenantCode ,
            "roleId" : roleid    
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete staff using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/role/delete", data=deleteroledata, headers=headers)
    if r.status_code == 200:
            print("role successfully deleted! : \n", r.json())
    else:
            print("role unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Bill API

def bill_Create():
    token = authentication_Login()
    createbillJSON = {
        "tenantCode" : tenantCode ,
        "payer" : {
              "name" : "auto bill generate test"
        },
        "amount" : "15.00" ,     
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/bill/create", json=createbillJSON, headers=headers)
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
        "tenantCode" : tenantCode ,
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/bill/list", params=billlistparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("bill list successfully retrieved! : \n", r_response)

    else:
        print("bill list unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def bill_View(billId):
    token = authentication_Login()
    viewbillparams = {
        "tenantCode" :tenantCode ,
        "billId" : billId 
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/bill/view", params=viewbillparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("bill successfully retrieved! : \n", r_response)

    else:
        print("bill unsuccessfully retrieved! : \n", r.status_code, r.text)


    return r.status_code

def bill_Update(billId):
    token = authentication_Login()
    updatebilldata = {
            "tenantCode" : tenantCode ,
            "billId" : billId ,
            "status" : "VOIDED"   
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/bill/update", data=updatebilldata, headers=headers)
    if r.status_code == 200:
            print("Bill successfully updated! : \n", r.json())
    else:
            print("Bill unsuccessfully updated! : \n", r.status_code, r.text)
    return r.status_code

#Staff: Tenant API
def tenant_View():
    token = authentication_Login()
    viewtenantparams = {
        "tenantCode" : tenantCode 
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/tenant/view", params=viewtenantparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("tenant successfully retrieved! : \n", r_response)

    else:
        print("tenant unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Tag API

def tag_List():
    token = authentication_Login()
    taglistparams = {
        "tenantCode" : tenantCode ,
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/tag/list", params=taglistparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("tag list successfully retrieved! : \n", r_response)

    else:
        print("tag list unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def tag_Create(tagname):
    token = authentication_Login()
    createtagdata = {
        "tenantCode" : tenantCode ,
        "name" : tagname,
        "color" : "#7732a8", #hex OR RGB formatting
        "type" : "PATIENT"
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/tag/create", data=createtagdata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("tag successfully created! : \n", r_response)
        tagid = r_response["result"]["tag"]["id"]
        print("Tag ID : ", tagid)

    else:
        print("tag unsuccessfully created: \n", r.status_code, r.text)


    return r.status_code,tagid

def tag_View(tagId):
    token = authentication_Login()
    viewtagparams = {
        "tenantCode" : tenantCode ,
        "tagId" : tagId
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/tag/view", params=viewtagparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("tag successfully retrieved! : \n", r_response)

    else:
        print("tag unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def tag_Update(tagId,tagname):
    token = authentication_Login()
    updatetagdata = {
            "tenantCode" : tenantCode ,
            "tagId" : tagId ,
            "name" : tagname   
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/tag/update", data=updatetagdata, headers=headers)
    if r.status_code == 200:
            print("Tag successfully updated! : \n", r.json())
    else:
            print("Tag unsuccessfully updated! : \n", r.status_code, r.text)
    return r.status_code

def tag_Delete(tagId):
    token = authentication_Login()
    deletetagdata = {
            "tenantCode" : tenantCode ,
            "tagId" : tagId    
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/tag/delete", data=deletetagdata, headers=headers)
    if r.status_code == 200:
            print("tag successfully deleted! : \n", r.json())
    else:
            print("tag unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Doctor Calendar Event API

def doctor_CalendarEvent_List(doctorId):
    token = authentication_Login()
    docCalendarEventListParams = {
        "tenantCode" : tenantCode ,
        "doctorId" : doctorId
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/doctor/calendarEvent/list", params=docCalendarEventListParams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Calendar Event list successfully retrieved! : \n", r_response)

    else:
        print("Calendar Event list unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def doctor_CalendarEvent_Create(doctorId,eventName):
    token = authentication_Login()
    #get current system time
    current_time = datetime.now()
    #Convert the date to ISO format
    iso_time = current_time.isoformat()
    createcalendareventdata = {
        "tenantCode" : tenantCode ,
        "doctorId" : doctorId,
        "name" : eventName,
        "action" : "BLOCK", #hex OR RGB formatting
        "startDate" : iso_time,
        "value" : "1",
        "type": "SPECIFIC"
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/doctor/calendarevent/create", data=createcalendareventdata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("Calendar Event successfully created! : \n", r_response)
        calendareventId = r_response["result"]["doctorCalendarEvent"]["id"]
        print("Calendar Event ID : ", calendareventId)

    else:
        print("Calendar Event unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code,calendareventId

def doctor_CalendarEvent_View(calendarEventId):
    token = authentication_Login()
    viewcalendareventparams = {
        "tenantCode" : tenantCode ,
        "doctorCalendarEventId" : calendarEventId
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/doctor/calendarevent/view", params=viewcalendareventparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Doctor Calendar Event successfully retrieved! : \n", r_response)

    else:
        print("Doctor Calendar Event unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def doctor_CalendarEvent_Update(calendarEventId,tagname):
    token = authentication_Login()
    #get current system time
    current_time = datetime.now()
    #Convert the date to ISO format
    iso_time = current_time.isoformat()
    updatecalendareventdata = {
            "tenantCode" : tenantCode ,
            "doctorCalendarEventId" : calendarEventId ,
            "startDate" : iso_time,
            "value" : "1",
            "name" : tagname   
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/doctor/calendarevent/update", data=updatecalendareventdata, headers=headers)
    if r.status_code == 200:
            print("Doctor Calendar Event successfully updated! : \n", r.json())
    else:
            print("Doctor Calendar Event unsuccessfully updated! : \n", r.status_code, r.text)
    return r.status_code

def doctor_CalendarEvent_Delete(calendarEventId):
    token = authentication_Login()
    deletecalendareventdata = {
            "tenantCode" : tenantCode ,
            "doctorCalendarEventId" : calendarEventId    
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/doctor/calendarevent/delete", data=deletecalendareventdata, headers=headers)
    if r.status_code == 200:
            print("Doctor Calendar Event successfully deleted! : \n", r.json())
    else:
            print("Doctor Calendar Event unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Service Calendar API

def service_Calendar_List(serviceId,month,year):
    token = authentication_Login()
    svcCalendarListParams = {
        "tenantCode" : tenantCode ,
        "serviceId" : serviceId,
        "month" : month,
        "year" : year
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/service/calendar/list", params=svcCalendarListParams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Service Calendar list successfully retrieved! : \n", r_response)

    else:
        print("Service Calendar list unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def service_Calendar_Appointment(serviceId,month,year):
    token = authentication_Login()
    svcCalendarApptsParams = {
        "tenantCode" : tenantCode ,
        "serviceIds" : {serviceId},
        "month" : month,
        "year" : year
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/service/calendar/appointment", params=svcCalendarApptsParams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Service Calendar appointments successfully retrieved! : \n", r_response)

    else:
        print("Service Calendar appointments unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def service_Calendar_timeslot(serviceId,branchId):
    token = authentication_Login()
    date_now = datetime.now()
    selectedDate = date_now.strftime("%Y-%m-%d")
    svcCalendarTimeslotParams = {
        "tenantCode" : tenantCode ,
        "serviceIds" : {serviceId},
        "branchId" : branchId,
        "selectedDate" : selectedDate
    }

    # Set the authorization header of the request

    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/service/calendar/timeslot", params=svcCalendarTimeslotParams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Service Calendar timeslot successfully retrieved! : \n", r_response)

    else:
        print("ServiceCalendar timeslot unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def service_Calendar_AvailableTimeslot(serviceId,branchId):
    token = authentication_Login()
    date_now = datetime.now()
    selectedDate = date_now.strftime("%Y-%m-%d")
    availabletimeslotparams = {
        "tenantCode" : tenantCode ,
        "serviceIds" : {serviceId},
        "branchId" : branchId,
        "selectedDate" : selectedDate
    }

    # Set the authorization header of the request

    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/service/calendar/availabletimeslot", params=availabletimeslotparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("service available timeslot successfully retrieved! : \n", r_response)

    else:
        print("service available timeslot unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

#Staff: Service API

def service_Create():
    token = authentication_Login()
    createservicedata = {
            "tenantCode" : tenantCode ,
            "name" : "Automation Service Ishlah" ,
            "code" : "AUTOService1" ,
            "branchIds" : "5608b972-2f93-4330-a2e8-83bad4c9fa84" #Default Branch
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create service using API AND store the response
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/service/create", data=createservicedata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
            print("Service successfully created! : \n", r_response)
            serviceid = r_response["result"]["service"]["id"]
            servicename = r_response ["result"]["service"]["name"]
            print("Service ID : ", serviceid)
            print("Service Name : ",servicename)
    else: 
            print("Service unsuccessfully failed: \n", r.status_code, r.text)


    return r.status_code,serviceid

def service_View(serviceId:str):
    token = authentication_Login()
    viewServiceParams = {
            "tenantCode" : tenantCode ,
            "serviceId" : serviceId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/service/view", params=viewServiceParams, headers=headers)

    if r.status_code == 200:
            print("Service details successfully retrieved! : \n", r.json())
    else:
            print("Service details unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def service_Update(serviceId:str):
    token = authentication_Login()
    updateServiceData = {
            "tenantCode" : tenantCode ,
            "serviceId" : serviceId,
            "name" : "update service auto",
            "code" : "AUTOHEHE",
            "branchIds" : "5608b972-2f93-4330-a2e8-83bad4c9fa84"
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update service using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/service/update", data=updateServiceData, headers=headers)

    if r.status_code == 200:
            print("Service details successfully updated! : \n", r.json())
    else:
            print("Service details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

def service_Delete(serviceId:str):
    token = authentication_Login()
    deleteservicedata = {
            "tenantCode" : tenantCode ,
            "serviceId" : serviceId
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, delete doctor using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/service/delete", data=deleteservicedata, headers=headers)

    if r.status_code == 200:
            print("service successfully deleted! : \n", r.json())
    else:
            print("service unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Service Calendar Event API

def Service_CalendarEvent_List(serviceId):
    token = authentication_Login()
    svcCalendarEventListParams = {
        "tenantCode" : tenantCode ,
        "serviceId" : serviceId
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/service/calendarEvent/list", params=svcCalendarEventListParams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Service Calendar Event list successfully retrieved! : \n", r_response)

    else:
        print("Service Calendar Event list unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def service_CalendarEvent_Create(serviceId,eventName):
    token = authentication_Login()
    #get current system time
    current_time = datetime.now()
    #Convert the date to ISO format
    iso_time = current_time.isoformat()
    svccreatecalendareventdata = {
        "tenantCode" : tenantCode ,
        "serviceId" : serviceId,
        "name" : eventName,
        "action" : "BLOCK", #hex OR RGB formatting
        "startDate" : iso_time,
        "value" : "1",
        "type": "SPECIFIC"
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/service/calendarevent/create", data=svccreatecalendareventdata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("Service Calendar Event successfully created! : \n", r_response)
        calendareventId = r_response["result"]["serviceCalendarEvent"]["id"]
        print("Service Calendar Event ID : ", calendareventId)

    else:
        print("Service Calendar Event unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code,calendareventId

def service_CalendarEvent_View(calendarEventId):
    token = authentication_Login()
    viewcalendareventparams = {
        "tenantCode" : tenantCode ,
        "serviceCalendarEventId" : calendarEventId
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/service/calendarevent/view", params=viewcalendareventparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Service Calendar Event successfully retrieved! : \n", r_response)

    else:
        print("Service Calendar Event unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def service_CalendarEvent_Update(calendarEventId,tagname):
    token = authentication_Login()
    #get current system time
    current_time = datetime.now()
    #Convert the date to ISO format
    iso_time = current_time.isoformat()
    updatecalendareventdata = {
            "tenantCode" : tenantCode ,
            "serviceCalendarEventId" : calendarEventId ,
            "startDate" : iso_time,
            "value" : "1",
            "name" : tagname   
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/service/calendarevent/update", data=updatecalendareventdata, headers=headers)
    if r.status_code == 200:
            print("service Calendar Event successfully updated! : \n", r.json())
    else:
            print("service Calendar Event unsuccessfully updated! : \n", r.status_code, r.text)
    return r.status_code

def service_CalendarEvent_Delete(calendarEventId):
    token = authentication_Login()
    deletecalendareventdata = {
            "tenantCode" : tenantCode ,
            "serviceCalendarEventId" : calendarEventId    
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/service/calendarevent/delete", data=deletecalendareventdata, headers=headers)
    if r.status_code == 200:
            print("Service Calendar Event successfully deleted! : \n", r.json())
    else:
            print("Service Calendar Event unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Doctor Calendar API
def doctor_Calendar_List(doctorId,month,year):
    token = authentication_Login()
    docCalendarListParams = {
        "tenantCode" : tenantCode ,
        "doctorId" : doctorId,
        "month" : month,
        "year" : year
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/doctor/calendar/list", params=docCalendarListParams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Calendar list successfully retrieved! : \n", r_response)

    else:
        print("Calendar list unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def doctor_Calendar_Appointment(doctorId,month,year):
    token = authentication_Login()
    docCalendarApptsParams = {
        "tenantCode" : tenantCode ,
        "doctorIds" : {doctorId},
        "month" : month,
        "year" : year
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/doctor/calendar/appointment", params=docCalendarApptsParams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Calendar appointments successfully retrieved! : \n", r_response)

    else:
        print("Calendar appointments unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def doctor_Calendar_timeslot(doctorId,branchId):
    token = authentication_Login()
    date_now = datetime.now()
    selectedDate = date_now.strftime("%Y-%m-%d")
    docCalendarTimeslotParams = {
        "tenantCode" : tenantCode ,
        "doctorIds" : {doctorId},
        "branchId" : branchId,
        "selectedDate" : selectedDate
    }

    # Set the authorization header of the request

    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/doctor/calendar/timeslot", params=docCalendarTimeslotParams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Calendar timeslot successfully retrieved! : \n", r_response)

    else:
        print("Calendar timeslot unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def doctor_Calendar_AvailableTimeslot(doctorId,branchId):
    token = authentication_Login()
    date_now = datetime.now()
    selectedDate = date_now.strftime("%Y-%m-%d")
    availabletimeslotparams = {
        "tenantCode" : tenantCode ,
        "doctorIds" : {doctorId},
        "branchId" : branchId,
        "selectedDate" : selectedDate
    }

    # Set the authorization header of the request

    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/doctor/calendar/availabletimeslot", params=availabletimeslotparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("available timeslot successfully retrieved! : \n", r_response)

    else:
        print("available timeslot unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

#Staff: Queue Screen API

def queue_Screen_List():
    token = authentication_Login()
    QSlistparams = {
        "tenantCode" : tenantCode 
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/queueScreen/list", params=QSlistparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Queue Screen list successfully retrieved! : \n", r_response)

    else:
        print("Queue Screen list unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def queue_Screen_Create(qsName,doctorId,qsUsername,qsPassword,status):
    token = authentication_Login()
    qsCreateData = {
        "tenantCode" : tenantCode ,
        "name" : qsName,
        "doctorIds" : {doctorId},
        "username" : qsUsername,
        "password" : qsPassword, 
        "status" : status
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/queueScreen/create", data=qsCreateData, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("Queue Screen successfully created! : \n", r_response)
        queueScreenId = r_response["result"]["queueScreen"]["id"]
        print("queue Screen ID : ", queueScreenId)

    else:
        print("Queue Screen unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code,queueScreenId

def queue_Screen_View(qsid):
    token = authentication_Login()
    viewQSParams = {
            "queueScreenId" : qsid,
            "tenantCode" : tenantCode 
            
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/queueScreen/view", params=viewQSParams, headers=headers)

    if r.status_code == 200:
            print("queue Screen successfully retrieved! : \n", r.json())
    else:
            print("queue Screen unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def queue_Screen_Update(queueScreenId,status):
    token = authentication_Login()
    qsUpdateData = {
            "tenantCode" : tenantCode ,
            "queueScreenId" : queueScreenId,
            "status" : status,
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update service using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/queueScreen/update", data=qsUpdateData, headers=headers)

    if r.status_code == 200:
            print("queue Screen details successfully updated! : \n", r.json())
    else:
            print("queue Screen details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

def queue_Screen_Delete(queueScreenId):
    token = authentication_Login()
    deleteQSdata = {
            "tenantCode" : tenantCode ,
            "queueScreenId" : queueScreenId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/queueScreen/delete", data=deleteQSdata, headers=headers)

    if r.status_code == 200:
            print("queue Screen successfully deleted! : \n", r.json())
    else:
            print("queue Screen unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Queue API

def queue_Create(queueName):
    token = authentication_Login()
    queueCreateData = {
        "tenantCode" : tenantCode ,
        "name" : queueName,
        "isPrimary" : "true"
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/queue/create", data=queueCreateData, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("Queue successfully created! : \n", r_response)
        queueId = r_response["result"]["queue"]["id"]
        print("queue ID : ", queueId)

    else:
        print("Queue unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code,queueId

def queue_View(queueId):
    token = authentication_Login()
    viewQueueParams = {
            "queueId" : queueId,
            "tenantCode" : tenantCode 
            
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/queue/view", params=viewQueueParams, headers=headers)

    if r.status_code == 200:
            print("queue successfully retrieved! : \n", r.json())
    else:
            print("queue unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def queue_Update(queueId,queueName):
    token = authentication_Login()
    queueUpdateData = {
            "tenantCode" : tenantCode ,
            "queueId" : queueId,
            "name" : queueName,
            "isPrimary" : "TRUE"
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update service using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/queue/update", data=queueUpdateData, headers=headers)

    if r.status_code == 200:
            print("queue details successfully updated! : \n", r.json())
    else:
            print("queue details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

def queue_delete(queueId):
    token = authentication_Login()
    deleteQdata = {
            "tenantCode" : tenantCode ,
            "queueId" : queueId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/queue/delete", data=deleteQdata, headers=headers)

    if r.status_code == 200:
            print("queue successfully deleted! : \n", r.json())
    else:
            print("queue unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Kiosk API
def kiosk_List():
    token = authentication_Login()
    kiosklistparams = {
        "tenantCode" : tenantCode 
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/kiosk/list", params=kiosklistparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("kiosk list successfully retrieved! : \n", r_response)

    else:
        print("kiosk list unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def kiosk_Create(kioskName,kioskUsername,kioskPassword):
    token = authentication_Login()
    kioskCreateData = {
        "tenantCode" : tenantCode ,
        "name" : kioskName,
        "username" :kioskUsername,
        "password" : kioskPassword,
        "status" : "ACTIVE"
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/kiosk/create", data=kioskCreateData, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("Kiosk successfully created! : \n", r_response)
        kioskId = r_response["result"]["kiosk"]["id"]
        print("kiosk ID : ", kioskId)

    else:
        print("Kiosk unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code,kioskId


def kiosk_View(kioskId):
    token = authentication_Login()
    viewKioskParams = {
            "kioskId" : kioskId,
            "tenantCode" : tenantCode 
            
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/kiosk/view", params=viewKioskParams, headers=headers)

    if r.status_code == 200:
            print("kiosk successfully retrieved! : \n", r.json())
    else:
            print("kiosk unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def kiosk_Update(kioskId,kioskName):
    token = authentication_Login()
    kioskUpdateData = {
            "tenantCode" : tenantCode ,
            "kioskId" : kioskId,
            "name" : kioskName
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update service using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/kiosk/update", data=kioskUpdateData, headers=headers)

    if r.status_code == 200:
            print("kiosk details successfully updated! : \n", r.json())
    else:
            print("kiosk details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

def kiosk_Delete(kioskId):
    token = authentication_Login()
    deletekioskdata = {
            "tenantCode" : tenantCode ,
            "kioskId" : kioskId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/kiosk/delete", data=deletekioskdata, headers=headers)

    if r.status_code == 200:
            print("kiosk successfully deleted! : \n", r.json())
    else:
            print("kiosk unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code


#Staff: News API

def news_List():
    token = authentication_Login()
    newslistparams = {
        "tenantCode" : tenantCode 
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/news/list", params=newslistparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("news list successfully retrieved! : \n", r_response)

    else:
        print("news list unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def news_Create(news_title,news_body):
    token = authentication_Login()
    newscreatedata = {
        "tenantCode" : tenantCode ,
        "title" : news_title,
        "body" :news_body
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/news/create", data=newscreatedata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("News successfully created! : \n", r_response)
        newsId = r_response["result"]["news"]["id"]
        print("News ID : ", newsId)

    else:
        print("Kiosk unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code,newsId

def news_View(newsId):
    token = authentication_Login()
    viewNewsParams = {
            "tenantCode": tenantCode,
            "newsId" : newsId
            
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/news/view", params=viewNewsParams, headers=headers)

    if r.status_code == 200:
            print("news successfully retrieved! : \n", r.json())
    else:
            print("news unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def news_Update(newsId,news_title):
    token = authentication_Login()
    newsupdatedata = {
            "tenantCode" : tenantCode ,
            "newsId" : newsId,
            "title" : news_title
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update service using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/news/update", data=newsupdatedata, headers=headers)

    if r.status_code == 200:
            print("news details successfully updated! : \n", r.json())
    else:
            print("news details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

def news_Delete(newsId):
    token = authentication_Login()
    deletenewsdata = {
            "tenantCode" : tenantCode ,
            "newsId" : newsId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/news/delete", data=deletenewsdata, headers=headers)

    if r.status_code == 200:
            print("news successfully deleted! : \n", r.json())
    else:
            print("news unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code


#Staff: Holiday API

def holiday_List(year):
    token = authentication_Login()
    holidaylistparams = {
        "tenantCode" : tenantCode,
        "year" : year
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/holiday/list", params=holidaylistparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("holiday list successfully retrieved! : \n", r_response)

    else:
        print("holiday list unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def holiday_Create(holiday_name,holiday_date,branchId):
    token = authentication_Login()
    holidaycreatedata = {
        "tenantCode" : tenantCode ,
        "name" : holiday_name,
        "selectedDate" :holiday_date,
        "status" : "ACTIVE",
        "branchIds" : {branchId}
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/holiday/create", data=holidaycreatedata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("Holiday successfully created! : \n", r_response)
        holidayId = r_response["result"]["holiday"]["id"]
        print("Holiday ID : ", holidayId)

    else:
        print("Holiday unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code,holidayId

def holiday_View(holidayId):
    token = authentication_Login()
    viewholidayparams = {
            "tenantCode": tenantCode,
            "holidayId" : holidayId
            
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/holiday/view", params=viewholidayparams, headers=headers)

    if r.status_code == 200:
            print("holiday successfully retrieved! : \n", r.json())
    else:
            print("holiday unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def holiday_Update(holidayId,holiday_name):
    token = authentication_Login()
    holidayupdatedata = {
            "tenantCode" : tenantCode ,
            "holidayId" : holidayId,
            "name" : holiday_name
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update service using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/holiday/update", data=holidayupdatedata, headers=headers)

    if r.status_code == 200:
            print("holiday details successfully updated! : \n", r.json())
    else:
            print("holiday details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

def holiday_Delete(holidayId):
    token = authentication_Login()
    deleteholidaydata = {
            "tenantCode" : tenantCode ,
            "holidayId" : holidayId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/holiday/delete", data=deleteholidaydata, headers=headers)

    if r.status_code == 200:
            print("holiday successfully deleted! : \n", r.json())
    else:
            print("holiday unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Form API
def form_List():
    token = authentication_Login()
    formlistparams = {
        "tenantCode" : tenantCode
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/form/list", params=formlistparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("form list successfully retrieved! : \n", r_response)

    else:
        print("form list unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def form_Create(form_title):
    token = authentication_Login()
    formcreatedata = {
        "tenantCode" : tenantCode ,
        "title" : form_title
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/form/create", data=formcreatedata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("form successfully created! : \n", r_response)
        formId = r_response["result"]["forms"]["id"]
        print("Form ID : ", formId)

    else:
        print("form unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code,formId

def form_View(formId):
    token = authentication_Login()
    viewformparams = {
            "tenantCode": tenantCode,
            "formId" : formId
            
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/form/view", params=viewformparams, headers=headers)

    if r.status_code == 200:
            print("Form successfully retrieved! : \n", r.json())
    else:
            print("Form unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def form_Update(formId,form_title):
    token = authentication_Login()
    formupdatejson = {
            "tenantCode" : tenantCode ,
            "formId" : formId,
            "title" : form_title,
            "items" : [
  {
    "type": "INPUT_TEXT",
    "label": "input text",
    "placeholder": "hi"
    },
    {
    "type": "INPUT_NUMBER",
    "label": "input number",
    "placeholder": "number"
    }
    ],
    
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update service using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/form/update", json=formupdatejson, headers=headers)

    if r.status_code == 200:
            print("form details successfully updated! : \n", r.json())
    else:
            print("form details unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

def form_Delete(formId):
    token = authentication_Login()
    deleteformdata = {
            "tenantCode" : tenantCode ,
            "formId" : formId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/form/delete", data=deleteformdata, headers=headers)

    if r.status_code == 200:
            print("form successfully deleted! : \n", r.json())
    else:
            print("form unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Form Submission API

def formSubmission_List(formId):
    token = authentication_Login()
    formsubmissionlistparams = {
        "tenantCode" : tenantCode,
        "formId" : formId
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/formSubmission/list", params=formsubmissionlistparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("form submission list successfully retrieved! : \n", r_response)

    else:
        print("form submisison list unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def formSubmission_Create(formId):
    token = authentication_Login()
    formsubmissioncreatedata = {
        "tenantCode" : tenantCode ,
        "formId" : formId
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/formSubmission/create", data=formsubmissioncreatedata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("form submission successfully created! : \n", r_response)
        formSubmissionId = r_response["result"]["formSubmission"]["id"]
        print("Form Submission ID : ", formSubmissionId)

    else:
        print("form Submission unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code,formSubmissionId

def formSubmission_View(formSubmissionId):
    token = authentication_Login()
    formsubmissionviewparams = {
            "tenantCode": tenantCode,
            "formSubmissionId" : formSubmissionId
            
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/formSubmission/view", params=formsubmissionviewparams, headers=headers)

    if r.status_code == 200:
            print("Form submission successfully retrieved! : \n", r.json())
    else:
            print("Form submission unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Template API

def template_Create():
    return

def template_View():
    return

def template_Update():
    return

def template_Delete():
    return

#Staff: Daily Note API

def dailyNote_List():
    token = authentication_Login()
    date_now = datetime.now()
    selectedDate = date_now.strftime("%Y-%m-%d")
    dailynotelistparams = {
        "tenantCode" : tenantCode,
        "selectedDate" : selectedDate
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/dailyNote/list", params=dailynotelistparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("daily note list successfully retrieved! : \n", r_response)

    else:
        print("daily note list unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code


def dailyNote_Create():
    token = authentication_Login()
    date_now = datetime.now()
    selectedDate = date_now.strftime("%Y-%m-%d")
    dailynotecreatedata = {
        "tenantCode" : tenantCode ,
        "selectedDate" : selectedDate,
        "content" : "Auto generated daily note"
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/dailyNote/create", data=dailynotecreatedata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("daily note successfully created! : \n", r_response)
        dailyNoteId = r_response["result"]["dailyNote"]["id"]
        print("Daily Note ID : ", dailyNoteId)

    else:
        print("Daily Note unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code,dailyNoteId

def dailyNote_View(dailyNoteId):
    token = authentication_Login()
    dailynoteviewparams = {
            "tenantCode": tenantCode,
            "dailyNoteId" : dailyNoteId
            
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/dailynote/view", params=dailynoteviewparams, headers=headers)

    if r.status_code == 200:
            print("daily Note successfully retrieved! : \n", r.json())
    else:
            print("Daily Note unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def dailyNote_Update(dailyNoteId):
    token = authentication_Login()
    dailynoteupdatedata = {
            "tenantCode" : tenantCode ,
            "dailyNoteId" : dailyNoteId,
            "contet" : "Updated auto generated daily note"
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update service using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/dailyNote/update", data=dailynoteupdatedata, headers=headers)

    if r.status_code == 200:
            print("daily note successfully updated! : \n", r.json())
    else:
            print("daily Note unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

def dailyNote_Delete(dailyNoteId):
    token = authentication_Login()
    deletedailynotedata = {
            "tenantCode" : tenantCode ,
            "dailyNoteId" : dailyNoteId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/dailyNote/delete", data=deletedailynotedata, headers=headers)

    if r.status_code == 200:
            print("daily note successfully deleted! : \n", r.json())
    else:
            print("daily note unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Location API
def location_List():
    token = authentication_Login()
    locationlistdata = {
        "tenantCode" : tenantCode 
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/location/list", data=locationlistdata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("location successfully retrieved! : \n", r_response)

    else:
        print("location unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code

def location_Create(location_name):
    token = authentication_Login()
    locationcreatedata = {
        "tenantCode" : tenantCode,
        "name" : location_name
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/location/create", data=locationcreatedata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("location successfully created! : \n", r_response)
        locationId = r_response["result"]["location"]["id"]
        print("location ID : ", locationId)

    else:
        print("location unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code,locationId

def location_View(locationId):
    token = authentication_Login()
    locationviewparams = {
            "tenantCode" : tenantCode ,
            "locationId" : locationId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/location/view", params=locationviewparams, headers=headers)

    if r.status_code == 200:
            print("Location details successfully retrieved! : \n", r.json())
    else:
            print("Location details unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code


def location_Update(locationId,location_name):
    token = authentication_Login()
    locationupdatedata = {
            "tenantCode" : tenantCode ,
            "locationId" : locationId,
            "name" : location_name
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update service using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/location/update", data=locationupdatedata, headers=headers)

    if r.status_code == 200:
            print("location successfully updated! : \n", r.json())
    else:
            print("location unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

def location_Delete(locationId):
    token = authentication_Login()
    deletelocationdata = {
            "tenantCode" : tenantCode ,
            "locationId" : locationId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/location/delete", data=deletelocationdata, headers=headers)

    if r.status_code == 200:
            print("location successfully deleted! : \n", r.json())
    else:
            print("location unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Visit Type API
def visit_type_List(doctorId):
    token = authentication_Login()
    visittypelistdata = {
        "tenantCode" : tenantCode ,
        "doctorId" : doctorId
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visitType/List", data=visittypelistdata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("visit type list successfully retrieved! : \n", r_response)
    else:
        print("visit type list unsuccessfully retrieved!: \n", r.status_code, r.text)

    return r.status_code

def visit_type_Create(doctorId,visit_type_name,visit_type_code):
    token = authentication_Login()
    visittypecreatedata = {
        "tenantCode" : tenantCode,
        "doctorId" : doctorId,
        "name": visit_type_name,
        "code" : visit_type_code,
        "status" : "ACTIVE"
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visitType/create", data=visittypecreatedata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("visit Type successfully created! : \n", r_response)
        visitTypeId = r_response["result"]["visitType"]["id"]
        print("Visit Type ID : ", visitTypeId)

    else:
        print("visit Type unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code,visitTypeId

def visit_type_View(visitTypeId):
    token = authentication_Login()
    visittypeviewparams = {
            "tenantCode" : tenantCode ,
            "visitTypeId" : visitTypeId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visitType/view", params=visittypeviewparams, headers=headers)

    if r.status_code == 200:
            print("visit type successfully retrieved! : \n", r.json())
    else:
            print("visit type unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code


def visit_type_Update(visitTypeId,visit_type_name):
    token = authentication_Login()
    visittypeupdatedata = {
            "tenantCode" : tenantCode ,
            "visitTypeId" : visitTypeId,
            "name" : visit_type_name
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update service using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visitType/update", data=visittypeupdatedata, headers=headers)

    if r.status_code == 200:
            print("visit type successfully updated! : \n", r.json())
    else:
            print("visit type unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code

def visit_type_Delete(visitTypeId):
    token = authentication_Login()
    deletevisittypedata = {
            "tenantCode" : tenantCode ,
            "visitTypeId" : visitTypeId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visitType/delete", data=deletevisittypedata, headers=headers)

    if r.status_code == 200:
            print("Visit Type successfully deleted! : \n", r.json())
    else:
            print("Visit Type unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code


#Visit Type Calendar API
def visitType_Calendar_List(visitTypeId,month,year):
    token = authentication_Login()
    visitTypeCalendarListParams = {
        "tenantCode" : tenantCode ,
        "visitTypeId" : visitTypeId,
        "month" : month,
        "year" : year
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visitType/calendar/list", params=visitTypeCalendarListParams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Visit Type Calendar list successfully retrieved! : \n", r_response)

    else:
        print("Visit Type Calendar list unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def visitType_Calendar_Appointment(visitTypeId,month,year):
    token = authentication_Login()
    visitTypeCalendarApptsParams = {
        "tenantCode" : tenantCode ,
        "visitTypeIds" : {visitTypeId},
        "month" : month,
        "year" : year
    }

    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visitType/calendar/appointment", params=visitTypeCalendarApptsParams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Visit Type Calendar appointments successfully retrieved! : \n", r_response)

    else:
        print("Visit Type Calendar appointments unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def visitType_Calendar_timeslot(visitTypeId):
    token = authentication_Login()
    date_now = datetime.now()
    selectedDate = date_now.strftime("%Y-%m-%d")
    visitTypeCalendarTimeslotParams = {
        "tenantCode" : tenantCode ,
        "visitTypeIds" : {visitTypeId},
        "selectedDate" : selectedDate
    }

    # Set the authorization header of the request

    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visitType/calendar/timeslot", params=visitTypeCalendarTimeslotParams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Visit Type Calendar timeslot successfully retrieved! : \n", r_response)

    else:
        print("Visit TypeCalendar timeslot unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def visitType_Calendar_AvailableTimeslot(visitTypeId):
    token = authentication_Login()
    date_now = datetime.now()
    selectedDate = date_now.strftime("%Y-%m-%d")
    availabletimeslotparams = {
        "tenantCode" : tenantCode ,
        "visitTypeIds" : {visitTypeId},
        "selectedDate" : selectedDate
    }

    # Set the authorization header of the request

    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visitType/calendar/availabletimeslot", params=availabletimeslotparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Visit Type available timeslot successfully retrieved! : \n", r_response)

    else:
        print("Visit Type available timeslot unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

#Visit Type Calendar Event API

def visitType_CalendarEvent_List(visitTypeId):
    token = authentication_Login()
    visitTypeCalendarEventListParams = {
        "tenantCode" : tenantCode ,
        "visitTypeId" : visitTypeId
    }
   
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visitType/calendarEvent/list", params=visitTypeCalendarEventListParams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("Visit Type Calendar Event list successfully retrieved! : \n", r_response)

    else:
        print("Visit Type Calendar Event list unsuccessfully retrieved: \n", r.status_code, r.text)
    return r.status_code

def visitType_CalendarEvent_Create(visitTypeId,eventName):
    token = authentication_Login()
    #get current system time
    current_time = datetime.now()
    #Convert the date to ISO format
    iso_time = current_time.isoformat()
    visittypecreatecalendareventdata = {
        "tenantCode" : tenantCode ,
        "visitTypeId" : visitTypeId,
        "name" : eventName,
        "action" : "BLOCK", #hex OR RGB formatting
        "startDate" : iso_time,
        "value" : "1",
        "type": "SPECIFIC"
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visitType/calendarevent/create", data=visittypecreatecalendareventdata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("visit Type Calendar Event successfully created! : \n", r_response)
        calendarEventId = r_response["result"]["visitTypeCalendarEvent"]["id"]
        print("visit Type Calendar Event ID : ", calendarEventId)

    else:
        print("Visit Type Calendar Event unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code,calendarEventId

def visitType_CalendarEvent_View(visitTypeCalendarEventId):
    token = authentication_Login()
    viewcalendareventparams = {
        "tenantCode" : tenantCode ,
        "visitTypeCalendarEventId" : visitTypeCalendarEventId
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visitType/calendarevent/view", params=viewcalendareventparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("visit Type Calendar Event successfully retrieved! : \n", r_response)

    else:
        print("Sevisit Typervice Calendar Event unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def visitType_CalendarEvent_Update(visitTypeCalendarEventId,tagname):
    token = authentication_Login()
    #get current system time
    current_time = datetime.now()
    #Convert the date to ISO format
    iso_time = current_time.isoformat()
    updatecalendareventdata = {
            "tenantCode" : tenantCode ,
            "visitTypeCalendarEventId" : visitTypeCalendarEventId ,
            "startDate" : iso_time,
            "value" : "1",
            "name" : tagname   
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visitType/calendarevent/update", data=updatecalendareventdata, headers=headers)
    if r.status_code == 200:
            print("visit Type Calendar Event successfully updated! : \n", r.json())
    else:
            print("visit Type Calendar Event unsuccessfully updated! : \n", r.status_code, r.text)
    return r.status_code

def visitType_CalendarEvent_Delete(visitTypeCalendarEventId):
    token = authentication_Login()
    deletecalendareventdata = {
            "tenantCode" : tenantCode ,
            "visitTypeCalendarEventId" : visitTypeCalendarEventId    
        }
     # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/visitType/calendarevent/delete", data=deletecalendareventdata, headers=headers)
    if r.status_code == 200:
            print("visit Type Calendar Event successfully deleted! : \n", r.json())
    else:
            print("visit Type Calendar Event unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code



#Staff: Checkpoint API
def checkpoint_List(doctorId):
    token = authentication_Login()
    checkpointlistparams = {
        "tenantCode" : tenantCode ,
        "doctorId" : doctorId,
        "statuses" : {
                "ACTIVE",
                "INACTIVE"
        }
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/checkpoint/list", params=checkpointlistparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("checkpoint list successfully retrieved! : \n", r_response)

    else:
        print("checkpoint list unsuccessfully retrieved: \n", r.status_code, r.text)


    return r.status_code

def checkpoint_Create(checkpoint_name,checkpoint_code,doctorId,branchId):
    token = authentication_Login()
    checkpointcreatedata = {
        "tenantCode" : tenantCode,
        "doctorId" : doctorId,
        "name": checkpoint_name,
        "code" : checkpoint_code,
        "branchId" : branchId,
        "status" : "ACTIVE"
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/checkpoint/create", data=checkpointcreatedata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("Checkpoint successfully created! : \n", r_response)
        checkpointId = r_response["result"]["checkpoint"]["id"]
        print("Checkpoint ID : ", checkpointId)

    else:
        print("Checkpoint unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code,checkpointId

def checkpoint_View(checkpointId):
    token = authentication_Login()
    checkpointviewparams = {
            "tenantCode" : tenantCode ,
            "checkpointId" : checkpointId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/checkpoint/view", params=checkpointviewparams, headers=headers)

    if r.status_code == 200:
            print("checkpoint successfully retrieved! : \n", r.json())
    else:
            print("checkpoint unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code


def checkpoint_Update(checkpointId,checkpoint_name):
    token = authentication_Login()
    checkpointupdatedata = {
            "tenantCode" : tenantCode ,
            "checkpointId" : checkpointId,
            "name" : checkpoint_name
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update service using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/checkpoint/update", data=checkpointupdatedata, headers=headers)

    if r.status_code == 200:
            print("checkpoint successfully updated! : \n", r.json())
    else:
            print("checkpoint unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code


def checkpoint_Delete(checkpointId):
    token = authentication_Login()
    checkpointdeletedata = {
            "tenantCode" : tenantCode ,
            "checkpointId" : checkpointId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/checkpoint/delete", data=checkpointdeletedata, headers=headers)

    if r.status_code == 200:
            print("checkpoint successfully deleted! : \n", r.json())
    else:
            print("checkpoint unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Department API
def department_List():
    token = authentication_Login()
    departmentlistparams = {
        "tenantCode" : tenantCode 
        
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, create staff using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/department/list", params=departmentlistparams, headers=headers)
    r_response = r.json()

    if r.status_code == 200:
        print("department list successfully retrieved! : \n", r_response)

    else:
        print("department list unsuccessfully retrieved: \n", r.status_code, r.text)


    return r.status_code

def department_Create(department_name):
    token = authentication_Login()
    departmentcreatedata = {
        "tenantCode" : tenantCode,
        "name" : department_name,
        "status" : "ACTIVE"
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    r = requests.post("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/department/create", data=departmentcreatedata, headers=headers)
    r_response = r.json()

    if r.status_code == 201:
        print("Department successfully created! : \n", r_response)
        departmentId = r_response["result"]["department"]["id"]
        print("Department ID : ", departmentId)

    else:
        print("Department unsuccessfully created: \n", r.status_code, r.text)

    return r.status_code,departmentId

def department_View(departmentId):
    token = authentication_Login()
    departmentviewparams = {
            "tenantCode" : tenantCode ,
            "departmentId" : departmentId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/department/view", params=departmentviewparams, headers=headers)

    if r.status_code == 200:
            print("department successfully retrieved! : \n", r.json())
    else:
            print("department unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code


def department_Update(departmentId,department_name):
    token = authentication_Login()
    departmentupdatedata = {
            "tenantCode" : tenantCode ,
            "departmentId" : departmentId,
            "name" : department_name
    }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, update service using API AND store the response
    r = requests.put("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/department/update", data=departmentupdatedata, headers=headers)

    if r.status_code == 200:
            print("department successfully updated! : \n", r.json())
    else:
            print("department unsuccessfully updated! : \n", r.status_code, r.text)

    return r.status_code


def department_Delete(departmentId):
    token = authentication_Login()
    departmentdeletedata = {
            "tenantCode" : tenantCode ,
            "departmentId" : departmentId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.delete("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/department/delete", data=departmentdeletedata, headers=headers)

    if r.status_code == 200:
            print("department successfully deleted! : \n", r.json())
    else:
            print("department unsuccessfully deleted! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Report Appointment API
def report_Appointment_Excel(doctorId,branchId):
    token = authentication_Login()
    reportapptexcelparams = {
            "tenantCode" : tenantCode ,
            "branchId" : branchId ,
            "doctorId" :doctorId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/report/appointment/excel", params=reportapptexcelparams, headers=headers)

    if r.status_code == 200:
            print("staff report appointment excel successfully retrieved! : \n", r.status_code)
    else:
            print("staff report appointment excel unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def report_Appointment_Statistic(doctorId,branchId):
    token = authentication_Login()
    reportapptstatsparams = {
            "tenantCode" : tenantCode ,
            "branchId" : branchId ,
            "doctorIds" :{doctorId}
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/report/appointment/statistic", params=reportapptstatsparams, headers=headers)

    if r.status_code == 200:
            print("staff report appointment statistic successfully retrieved! : \n", r.status_code)
    else:
            print("staff report appointment statistic unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def report_Appointment_Dashboard(doctorId,branchId):
    token = authentication_Login()
    reportapptdashboardparams = {
            "tenantCode" : tenantCode ,
            "branchId" : branchId ,
            "doctorId" :{doctorId}
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/report/appointment/dashboard", params=reportapptdashboardparams, headers=headers)

    if r.status_code == 200:
            print("staff report appointment dashboard successfully retrieved! : \n", r.status_code)
    else:
            print("staff report appointment dashboard  unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def report_Appointment_CustomStatus(doctorId,branchId,startDate,endDate):
    token = authentication_Login()
    reportapptcustomstatusparams = {
            "tenantCode" : tenantCode ,
            "branchId" : branchId ,
            "doctorId" :{doctorId},
            "startDate" : startDate ,
            "endDate" : endDate
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/report/appointment/customStatus", params=reportapptcustomstatusparams, headers=headers)

    if r.status_code == 200:
            print("report appointment custom status successfully retrieved! : \n", r.status_code)
    else:
            print("report appointment custom status  unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Report Visit API

def report_Visit_miaSummary(branchId,doctorId,startDate,endDate):
    token = authentication_Login()
    miasummaryparams = {
            "tenantCode" : tenantCode ,
            "branchId" : branchId ,
            "doctorIds" :{doctorId},
            "startDate" : startDate ,
            "endDate" : endDate
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/report/visit/miaSummary", params=miasummaryparams, headers=headers)

    if r.status_code == 200:
            print("report visit MIA Summary successfully retrieved! : \n", r.status_code)
    else:
            print("report visit MIA Summary unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code


def report_Visit_QueueList(branchId,doctorId,startDate,endDate):
    token = authentication_Login()
    queuelistparams = {
            "tenantCode" : tenantCode ,
            "branchId" : branchId ,
            "doctorIds" :{doctorId},
            "startDate" : startDate ,
            "endDate" : endDate
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/report/visit/queueList", params=queuelistparams, headers=headers)

    if r.status_code == 200:
            print("report visit queue list successfully retrieved! : \n", r.status_code)
    else:
            print("report visit queue list unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def report_Visit_Duration(branchId,doctorId,startDate,endDate):
    token = authentication_Login()
    durationparams = {
            "tenantCode" : tenantCode ,
            "branchId" : branchId ,
            "doctorIds" :{doctorId},
            "startDate" : startDate ,
            "endDate" : endDate
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/report/visit/duration", params=durationparams, headers=headers)

    if r.status_code == 200:
            print("report visit duration successfully retrieved! : \n", r.status_code)
    else:
            print("report visit duration unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Report Staff API

def report_Staff_ApptVisitSummary(branchId,doctorId,startDate,endDate):
    token = authentication_Login()
    apptvisitsummaryparams = {
            "tenantCode" : tenantCode ,
            "branchId" : branchId ,
            "doctorIds" :{doctorId},
            "startDate" : startDate ,
            "endDate" : endDate
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/report/staff/appointmentvisitsummary", params=apptvisitsummaryparams, headers=headers)

    if r.status_code == 200:
            print("report staff appointment visit summary successfully retrieved! : \n", r.status_code)
    else:
            print("report staff appointment visit summary unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Log API
def auditLog_List():
    token = authentication_Login()
    auditlogparams = {
            "tenantCode" : tenantCode 
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/log/audit/list", params=auditlogparams, headers=headers)

    if r.status_code == 200:
            print("Audit Log List successfully retrieved! : \n", r.json())
    else:
            print("Audit Log List unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def patientLog_List(patientId):
    token = authentication_Login()
    patientlogparams = {
            "tenantCode" : tenantCode ,
            "patientId" : patientId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/log/patient/list", params=patientlogparams, headers=headers)

    if r.status_code == 200:
            print("patient Log List successfully retrieved! : \n", r.json())
    else:
            print("patient Log List unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Constant API

def constant_creatorType():
    token = authentication_Login()
    creatortypeparams = {
            "tenantCode" : tenantCode 
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/constant/creatortype", params=creatortypeparams, headers=headers)

    if r.status_code == 200:
            print("creator type List successfully retrieved! : \n", r.json())
    else:
            print("creator type List unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def constant_logAuditAction():
    token = authentication_Login()
    logauditactionparams = {
            "tenantCode" : tenantCode 
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/constant/logauditaction", params=logauditactionparams, headers=headers)

    if r.status_code == 200:
            print("log audit actions successfully retrieved! : \n", r.json())
    else:
            print("log audit actions unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

def constant_logAuditModule():
    token = authentication_Login()
    logauditmoduleparams = {
            "tenantCode" : tenantCode 
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/constant/logauditmodule", params=logauditmoduleparams, headers=headers)

    if r.status_code == 200:
            print("log audit modules successfully retrieved! : \n", r.json())
    else:
            print("log audit modules unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code


#Staff: Visit Log API
def visitLog_List():
    token = authentication_Login()
    visitlogparams = {
            "tenantCode" : tenantCode 
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/log/visit/list", params=visitlogparams, headers=headers)

    if r.status_code == 200:
            print("Visit Log List successfully retrieved! : \n", r.json())
    else:
            print("Visit Log List unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Appointment Log API
def appointmentLog_list():
    token = authentication_Login()
    appointmentlogparams = {
            "tenantCode" : tenantCode 
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/log/appointment/list", params=appointmentlogparams, headers=headers)

    if r.status_code == 200:
            print("Appointment Log List successfully retrieved! : \n", r.json())
    else:
            print("Appointment Log List unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Email Log API
def emailLog_List(pageCount,limitCount):
    token = authentication_Login()
    emaillogparams = {
            "tenantCode" : tenantCode ,
            "page" : pageCount,
            "limit" : limitCount,
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/log/email/list", params=emaillogparams, headers=headers)

    if r.status_code == 200:
            print("Email Log List successfully retrieved! : \n", r.json())
    else:
            print("Email Log List unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

#Staff: SMS Log API
def smsLog_List(pageCount,limitCount):
    token = authentication_Login()
    smslogparams = {
            "tenantCode" : tenantCode ,
            "page" : pageCount,
            "limit" : limitCount,
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/log/sms/list", params=smslogparams, headers=headers)

    if r.status_code == 200:
            print("SMS Log List successfully retrieved! : \n", r.json())
    else:
            print("SMS Log List unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code

#Staff: Integration Log API

def integrationLog_List(pageCount,limitCount):
    token = authentication_Login()
    integrationlogparams = {
            "tenantCode" : tenantCode ,
            "page" : pageCount,
            "limit" : limitCount,
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/log/integration/list", params=integrationlogparams, headers=headers)

    if r.status_code == 200:
            print("Integration Log List successfully retrieved! : \n", r.json())
    else:
            print("Integration Log List unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code
#Staff: Workflow Log API
def workflowLog_List(pageCount,limitCount,type):
    token = authentication_Login()
    workflowlogparams = {
            "tenantCode" : tenantCode ,
            "page" : pageCount,
            "limit" : limitCount,
            "type" : type
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/log/workflow/list", params=workflowlogparams, headers=headers)

    if r.status_code == 200:
            print("Workflow Log List successfully retrieved! : \n", r.json())
    else:
            print("Workflow Log List unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code
#Staff: Voucher log API
def voucherLog_List(pageCount,limitCount):
    token = authentication_Login()
    voucherlogparams = {
            "tenantCode" : tenantCode ,
            "page" : pageCount,
            "limit" : limitCount,
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/log/voucher/list", params=voucherlogparams, headers=headers)

    if r.status_code == 200:
            print("Voucher Log List successfully retrieved! : \n", r.json())
    else:
            print("Voucher Log List unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code


#Staff: Branch API
def branch_List():
    token = authentication_Login()
    branchlistparams = {
            "tenantCode" : tenantCode 
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/branch/list", params=branchlistparams, headers=headers)

    if r.status_code == 200:
            print("branch list successfully retrieved! : \n", r.json())
    else:
            print("branch list unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code
def branch_View(branchId):
    token = authentication_Login()
    branchviewparams = {
            "tenantCode" : tenantCode ,
            "branchId" : branchId
        }
    # Set the authorization header of the request
    headers = {"Authorization" : f"Bearer {token}"}
    #using requests library, retrieve doctor details using API AND store the response
    r = requests.get("https://staffhub-dev.encoremed.io/api/v1/ttish/staff/branch/view", params=branchviewparams, headers=headers)

    if r.status_code == 200:
            print("branch details successfully retrieved! : \n", r.json())
    else:
            print("branch details unsuccessfully retrieved! : \n", r.status_code, r.text)

    return r.status_code
