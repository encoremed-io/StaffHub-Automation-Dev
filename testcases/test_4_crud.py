from utilities.crud import *

def testCRUD_Doctor():

    #create doctor API
    createDoctorAPI_resp,doctorid,doctorname = createDoctor()
    assert createDoctorAPI_resp == 201 , "Create Doctor API failed"
    
    #view (read) doctor API
    assert viewDoctor(doctorid,"pah") == 200

    #update doctor API
    updateDoctorAPI_resp = updateDoctor("pah",doctorid)
    assert updateDoctorAPI_resp == 200, "update Doctor API failed"
    
    #delete doctor API
    deleteDoctorAPI_resp = deleteDoctor(doctorid,"pah")
    assert deleteDoctorAPI_resp == 200, "Delete Doctor API failed"
    