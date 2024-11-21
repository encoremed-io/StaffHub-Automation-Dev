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


def patient_Create():
    token = authentication_Login()

    patientdata = {
            "tenantCode" : tenantCode , 
            "name" : "Ishlah Test Auto",
            "identityNo" : 50505050
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
    },
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



