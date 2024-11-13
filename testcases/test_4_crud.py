from utilities.crud import *

def testCRUD_Doctor():

    #create doctor API
    createDoctorAPI_resp,doctorId = doctor_Create()
    assert createDoctorAPI_resp == 201 , "Create Doctor API failed"
    
    #view (read) doctor API
    assert doctor_View("pah",doctorId) == 200, "Retrieve Doctor API failed"

    #update doctor API
    updateDoctorAPI_resp = doctor_Update("pah",doctorId)
    assert updateDoctorAPI_resp == 200, "update Doctor API failed"
    
    #delete doctor API
    deleteDoctorAPI_resp = doctor_Delete("pah",doctorId)
    assert deleteDoctorAPI_resp == 200, "Delete Doctor API failed"
    
def testCRUD_Patient():
    
    #create patient API
    createPatientAPI_resp,patientId = patient_Create()
    assert createPatientAPI_resp == 201 , "Create Patient API failed"

    #view (read) patient API
    assert patient_View("pah",patientId) == 200, "Retrieve patient API failed"

    #update patient API
    updatePatientAPI_resp = patient_Update("pah",patientId)
    assert updatePatientAPI_resp == 200, "update Patient API failed"
    
    #delete patient API
    deletePatientAPI_resp = patient_Delete("pah",patientId)
    assert deletePatientAPI_resp == 200, "Delete Patient API failed"

def testCRUD_Staff():
    #create Staff API
    createStaffAPI_resp,staffId = staff_Create()
    assert createStaffAPI_resp == 201 , "Create Patient API failed"

    #view (read) Staff API
    assert staff_View("pah",staffId) == 200, "Retrieve Staff API failed"

    #update staff API
    updateStaffAPI_resp = staff_Update("pah",staffId)
    assert updateStaffAPI_resp == 200, "update Patient API failed"
    
    #delete staff API
    deleteStaffAPI_resp = staff_Delete("pah",staffId)
    assert deleteStaffAPI_resp == 200, "Delete Patient API failed"
    
# def testCRUD_Visit():

def testCRUD_Appointment():

    #create appointment API
    createApptAPI_resp,apptid = appointment_Create()
    assert createApptAPI_resp == 201,"Create Appointment API failed"

    #view (read) appointment api
    assert appointment_View("pah",apptid) == 200, "Retrieve Appointment API failed"


    #update appointment API
    updateApptAPI_resp = appointment_Update("pah",apptid)
    assert updateApptAPI_resp == 200, "update Appointment API failed"

    #delete appointment API
    deleteApptAPI_resp = appointment_Delete("pah",apptid)
    assert deleteApptAPI_resp == 200, "delete Appointment API failed"

def testCRUD_Visit():

    #create Visit API
    createVisitAPI_resp,visitid = visit_Create()
    assert createVisitAPI_resp == 201,"Create Visit API failed"

    #view (read) Visit api
    assert visit_View("pah",visitid) == 200, "view Visit API failed"


    #update Visit API
    updateVisitAPI_resp = visit_Update("pah",visitid)
    assert updateVisitAPI_resp == 200, "update Visit API failed"

    #delete Visit API
    deleteVisitAPI_resp = visit_Delete("pah",visitid)
    assert deleteVisitAPI_resp == 200, "delete Visit API failed"

def testCRUD_StaffProfile():

    #View Staff Profile API
    assert staffProfile_View("pah") == 200, "View Staff Profile API failed"

    #update Staff password API
    staffProfilePasswordAPI_resp = staffProfile_password("pah")
    assert staffProfilePasswordAPI_resp == 200 , "Update Password Staff Profile API failed"

    #update Staff profile API
    staffProfileUpdateAPI_resp = staffProfile_Update("pah","try update staff profile name")
    assert staffProfileUpdateAPI_resp == 200, "Update Staff Profile API"
