from utilities.crud import *

def testCRUD_Doctor():

    #create doctor API
    createDoctorAPI_resp,doctorId = createDoctor()
    assert createDoctorAPI_resp == 201 , "Create Doctor API failed"
    
    #view (read) doctor API
    assert viewDoctor("pah",doctorId) == 200, "Retrieve Doctor API failed"

    #update doctor API
    updateDoctorAPI_resp = updateDoctor("pah",doctorId)
    assert updateDoctorAPI_resp == 200, "update Doctor API failed"
    
    #delete doctor API
    deleteDoctorAPI_resp = deleteDoctor("pah",doctorId)
    assert deleteDoctorAPI_resp == 200, "Delete Doctor API failed"
    
def testCRUD_Patient():
    
    #create patient API
    createPatientAPI_resp,patientId = createPatient()
    assert createPatientAPI_resp == 201 , "Create Patient API failed"

    #view (read) patient API
    assert viewPatient("pah",patientId) == 200, "Retrieve patient API failed"

    #update patient API
    updatePatientAPI_resp = updatePatient("pah",patientId)
    assert updatePatientAPI_resp == 200, "update Patient API failed"
    
    #delete patient API
    deletePatientAPI_resp = deletePatient("pah",patientId)
    assert deletePatientAPI_resp == 200, "Delete Patient API failed"

def testCRUD_Staff():
    #create Staff API
    createStaffAPI_resp,staffId = createStaff()
    assert createStaffAPI_resp == 201 , "Create Patient API failed"

    #view (read) Staff API
    assert viewStaff("pah",staffId) == 200, "Retrieve Staff API failed"

    #update staff API
    updateStaffAPI_resp = updateStaff("pah",staffId)
    assert updateStaffAPI_resp == 200, "update Patient API failed"
    
    #delete staff API
    deleteStaffAPI_resp = deleteStaff("pah",staffId)
    assert deleteStaffAPI_resp == 200, "Delete Patient API failed"
    
# def testCRUD_Visit():

# def testCRUD_Appointment():
    