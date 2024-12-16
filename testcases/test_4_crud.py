from utilities.crud import *

def testCRUD_Staff_Authentication():
    
    #login API
    token = authentication_Login()
    assert (token is not None) ,"Login API failed"

    #forgot password API
    forgotPasswordAPI_resp = authentication_Forgot_Password()

 

def testCRUD_Doctor():

    #create doctor API
    createDoctorAPI_resp,doctorId = doctor_Create()
    assert createDoctorAPI_resp == 201 , "Create Doctor API failed"
    
    #view (read) doctor API
    assert doctor_View(doctorId) == 200, "Retrieve Doctor API failed"

    #update doctor API
    updateDoctorAPI_resp = doctor_Update(doctorId)
    assert updateDoctorAPI_resp == 200, "update Doctor API failed"
    
    #delete doctor API
    deleteDoctorAPI_resp = doctor_Delete(doctorId)
    assert deleteDoctorAPI_resp == 200, "Delete Doctor API failed"
    
def testCRUD_Patient():
    
    #create patient API
    createPatientAPI_resp,patientId = patient_Create()
    assert createPatientAPI_resp == 201 , "Create Patient API failed"

    #view (read) patient API
    assert patient_View(patientId) == 200, "Retrieve patient API failed"

    #update patient API
    updatePatientAPI_resp = patient_Update(patientId)
    assert updatePatientAPI_resp == 200, "update Patient API failed"
    
    #delete patient API
    deletePatientAPI_resp = patient_Delete(patientId)
    assert deletePatientAPI_resp == 200, "Delete Patient API failed"

def testCRUD_Staff():

    #retrieve Staff List API
    staffListAPI_resp = staff_List()
    assert staffListAPI_resp == 200, "Staff List API failed"

    #create Staff API
    createStaffAPI_resp,staffId = staff_Create()
    assert createStaffAPI_resp == 201 , "Create Patient API failed"

    #view (read) Staff API
    assert staff_View(staffId) == 200, "Retrieve Staff API failed"

    #update staff API
    updateStaffAPI_resp = staff_Update(staffId)
    assert updateStaffAPI_resp == 200, "update Patient API failed"
    
    #delete staff API
    deleteStaffAPI_resp = staff_Delete(staffId)
    assert deleteStaffAPI_resp == 200, "Delete Patient API failed"
    

def testCRUD_Appointment():

    #create appointment API
    createApptAPI_resp,apptid = appointment_Create()
    assert createApptAPI_resp == 201,"Create Appointment API failed"

    #view (read) appointment api
    assert appointment_View(apptid) == 200, "Retrieve Appointment API failed"


    #update appointment API
    updateApptAPI_resp = appointment_Update(apptid)
    assert updateApptAPI_resp == 200, "update Appointment API failed"

    #delete appointment API
    deleteApptAPI_resp = appointment_Delete(apptid)
    assert deleteApptAPI_resp == 200, "delete Appointment API failed"

#Staff: Visit API
def testCRUD_Visit():

    #create Visit API
    createVisitAPI_resp,visitid,visitPatientId = visit_Create()
    assert createVisitAPI_resp == 201,"Create Visit API failed"

    #view (read) Visit api
    assert visit_View(visitid) == 200, "view Visit API failed"

    #update Visit API
    updateVisitAPI_resp = visit_Update(visitid)
    assert updateVisitAPI_resp == 200, "update Visit API failed"

    #delete Visit API
    deleteVisitAPI_resp = visit_Delete(visitid)
    assert deleteVisitAPI_resp == 200, "delete Visit API failed"
    patient_Delete(visitPatientId)

def testCRUD_StaffProfile():

    #View Staff Profile API
    assert staffProfile_View() == 200, "View Staff Profile API failed"

    #update Staff password API
    staffProfilePasswordAPI_resp = staffProfile_password()
    assert staffProfilePasswordAPI_resp == 200 , "Update Password Staff Profile API failed"

    #update Staff profile API
    staffProfileUpdateAPI_resp = staffProfile_Update("try update staff profile name")
    assert staffProfileUpdateAPI_resp == 200, "Update Staff Profile API"

    #revert back to original staff profile name
    staffProfile_Update("Ishlah")

def testCRUD_Role():

    
    #Create Role API
    createRoleAPI_resp,roleid = role_Create("test role auto")
    assert createRoleAPI_resp == 201 , "Create Role API failed"

    #View Role API
    viewRoleAPI_resp = role_View(roleid)
    assert viewRoleAPI_resp == 200, "View Role API failed"

    #update Role API
    updateRoleAPI_resp = role_Update(roleid,"test role auto updated")
    assert updateRoleAPI_resp == 200 , "update Role API fialed"

    #delete Role API
    deleteRoleAPI_resp = role_Delete(roleid)
    assert deleteRoleAPI_resp == 200 , "Delete Role API failed"

def testCRUD_Bill():

    #View Bill List API
    billListAPI_resp = bill_List()
    assert billListAPI_resp == 200 , "View Bill List API failed"

    #Create Bill API
    createBillAPI_resp,billId = bill_Create()
    assert createBillAPI_resp == 201, "Create Bill API failed"

    #View Bill API
    viewBillAPI_resp = bill_View(billId)
    assert viewBillAPI_resp == 200, "View Bill API failed"

    #Update Bill API
    updateBillAPI_resp = bill_Update(billId)
    assert updateBillAPI_resp == 200, "update Bill API failed"


def testCRUD_Tenant():

    #View Tenant API
    viewTenantAPI_resp = tenant_View()
    assert viewTenantAPI_resp == 200,"View Tenant API failed"

def testCRUD_Tag():

    #view Tag List API
    tagListAPI_resp = tag_List()
    assert tagListAPI_resp == 200 , "View Tag List API failed"

    #create Tag API
    createTagAPI_resp,tagId = tag_Create("auto tag")
    assert createTagAPI_resp == 201 , "Create Tag API failed"

    #view Tag API
    viewTagAPI_resp = tag_View(tagId)
    assert viewTagAPI_resp == 200, "View Tag API failed"

    #Update Tag API
    updateTagAPI_resp = tag_Update(tagId,"updated auto tag")
    assert updateTagAPI_resp == 200,"Update Tag API failed"

    #delete Tag API
    deleteTagAPI_resp = tag_Delete(tagId)
    assert deleteTagAPI_resp == 200, "Delete Tag API failed"


def testCRUD_Doctor_Calendar_Event():
    
    #pre-requisite : Doctor ID is required. 
    x,doctorId = doctor_Create()

    try:
        #View Doctor Calendar Event List API
        calendarEventListAPI_resp = doctor_CalendarEvent_List(doctorId)
        assert calendarEventListAPI_resp == 200,"View Doctor Calendar Event List API failed"

        #Create Doctor Calendar Event API
        createCalendarEventAPI_resp, calendarEventId = doctor_CalendarEvent_Create(doctorId,"auto Calendar Event")
        assert createCalendarEventAPI_resp== 201, "Create Doctor Calendar Event API failed"

        #View Doctor Calendar Event API
        viewCalendarEventAPI_resp = doctor_CalendarEvent_View(calendarEventId)
        assert viewCalendarEventAPI_resp == 200, "View Doctor Calendar Event API failed"

        #Update Doctor Calendar Event API
        updateCalendarEventAPI_resp = doctor_CalendarEvent_Update(calendarEventId,"updated Doctor Calendar Event")
        assert updateCalendarEventAPI_resp == 200, "Update Doctor Calendar Event API failed"
        
        #Delete Doctor Calendar Event API
        deleteCalendarEventAPI_resp = doctor_CalendarEvent_Delete(calendarEventId)
        assert deleteCalendarEventAPI_resp == 200,"Delete Doctor Calendar Event API failed"
    finally:
        #delete doctor at the end
        doctor_Delete(doctorId)

def testCRUD_Doctor_Calendar():

    try:
        #pre-requisite - need a doctor first
        x,doctorId = doctor_Create()
        
        #View Doctor Calendar List API
        assert doctor_Calendar_List(doctorId,11,2024) == 200,"Doctor Calendar List API failed"

        #View Doctor Calendar Appointment API
        assert doctor_Calendar_Appointment(doctorId,11,2024)==200, "Doctor Calendar Appointment API failed"

        #View Doctor Calendar Timeslot API
        assert doctor_Calendar_timeslot(doctorId,"5608b972-2f93-4330-a2e8-83bad4c9fa84") == 200, " Doctor Calendar Timeslot API failed"

        #View Doctor Calendar Available Timeslot API
        assert doctor_Calendar_AvailableTimeslot(doctorId,"5608b972-2f93-4330-a2e8-83bad4c9fa84") == 200, "Doctor Calendar Available Timeslot API failed"
    finally:
        #delete doctor
        doctor_Delete(doctorId)

def testCRUD_Service():

    #Create Service API
    servicecreateAPI_resp,serviceId = service_Create()
    assert servicecreateAPI_resp == 201, "Service Create API failed"

    #View Service API
    serviceviewAPI_resp = service_View(serviceId)
    assert serviceviewAPI_resp == 200, "Service View API failed"

    #Update Service API
    serviceupdateAPI_resp = service_Update(serviceId)
    assert serviceupdateAPI_resp == 200, "Service Update API failed"

    #Delete Service API
    servicedeleteAPI_resp = service_Delete(serviceId)
    assert servicedeleteAPI_resp == 200, "Service Delete API failed"    

def testCRUD_Service_Calendar_Event():
        
    #pre-requisite : Service ID is required. 
    x,serviceId = service_Create()

    try:
        #View Service Calendar Event List API
        calendarEventListAPI_resp = Service_CalendarEvent_List(serviceId)
        assert calendarEventListAPI_resp == 200,"View Service Calendar Event List API failed"

        #Create Service Calendar Event API
        createCalendarEventAPI_resp, calendarEventId = service_CalendarEvent_Create(serviceId,"auto Calendar Event")
        assert createCalendarEventAPI_resp== 201, "Create Service Calendar Event API failed"

        #View Service Calendar Event API
        viewCalendarEventAPI_resp = service_CalendarEvent_View(calendarEventId)
        assert viewCalendarEventAPI_resp == 200, "View Service Calendar Event API failed"

        #Update Service Calendar Event API
        updateCalendarEventAPI_resp = service_CalendarEvent_Update(calendarEventId,"updated Service Calendar Event")
        assert updateCalendarEventAPI_resp == 200, "Update Service Calendar Event API failed"
        
        #Delete Service Calendar Event API
        deleteCalendarEventAPI_resp = service_CalendarEvent_Delete(calendarEventId)
        assert deleteCalendarEventAPI_resp == 200,"Delete service Calendar Event API failed"
    finally:
        #delete Service at the end
        service_Delete(serviceId)

def testCRUD_Service_Calendar():

    try:
        #pre-requisite - need a service first
        x,serviceId = service_Create()
        
        #View Service Calendar List API
        assert service_Calendar_List(serviceId,11,2024) == 200,"Service Calendar List API failed"

        #View Service Calendar Appointment API
        assert service_Calendar_Appointment(serviceId,11,2024)==200, "Service Calendar Appointment API failed"

        #View Service Calendar Timeslot API
        assert service_Calendar_timeslot(serviceId,"5608b972-2f93-4330-a2e8-83bad4c9fa84")==200, " Service Calendar Timeslot API failed"

        #View Service Calendar Available Timeslot API
        assert service_Calendar_AvailableTimeslot(serviceId,"5608b972-2f93-4330-a2e8-83bad4c9fa84") ==200, "Service Calendar Available Timeslot API failed"
    finally:
        #delete Service
        service_Delete(serviceId)


def testCRUD_Queue_Screen():
    try:
        #pre-requisite : doctor
        x,doctorId=doctor_Create()
        #View Queue Screen List API
        assert queue_Screen_List() == 200,"Queue Screen List API failed"

        #Create Queue Screen API
        createqueuescreenAPI_resp,queueScreenId= queue_Screen_Create("auto queue screen",doctorId,"ishlahQS","1Aaaaaaa","ACTIVE")
        assert createqueuescreenAPI_resp == 201,"Create Queue Screen API failed"
        #View Queue Screen API
        assert queue_Screen_View(queueScreenId) == 200, " View Queue Screen API failed"

        #Update Queue Screen API
        assert queue_Screen_Update(queueScreenId,"INACTIVE") == 200, "update Queue Screen API failed"

        #Delete Queue Screen API
        assert queue_Screen_Delete(queueScreenId)==200,"Delete Queue Screen API failed"
    
    finally:
        doctor_Delete(doctorId)
        
def testCRUD_Queue():

    #Create Queue API
    createQueueAPI_resp,queueId = queue_Create("Auto Queue")
    assert createQueueAPI_resp==201,"Create Queue API failed"

    #View Queue API
    assert queue_View(queueId) == 200, "View Queue API failed"

    #Update Queue API
    updateQueueAPI_resp = queue_Update(queueId,"updated Auto Queue")
    assert updateQueueAPI_resp == 200, "Update Queue API failed"

    #Delete Queue API
    deleteQueueAPI_resp = queue_delete(queueId)
    assert deleteQueueAPI_resp == 200, "Delete Queue API failed"

def testCRUD_Kiosk():

    #Kiosk List API
    assert kiosk_List() == 200,"Kiosk List API failed"

    #Create Kiosk List API
    createKioskAPI_resp,kioskId = kiosk_Create("Auto Kiosk",username,password)
    assert createKioskAPI_resp == 201, "create Kiosk API failed"
    
    #View Kiosk API
    assert kiosk_View(kioskId) == 200, "View Kiosk API failed"

    #Update Kiosk API
    updateKioskAPI_resp = kiosk_Update(kioskId,"updated auto kiosk")
    assert updateKioskAPI_resp == 200, "Update Kiosk API failed"

    #Delete Kiosk API
    assert kiosk_Delete(kioskId) == 200, "Delete Kiosk API failed"

def testCRUD_News():

    #News List API
    assert news_List() == 200,"News List API failed"

    #Create News API
    createNewsAPI_resp,newsId = news_Create("Auto News Title","Auto News Body")
    assert createNewsAPI_resp == 201, "create News API failed"
    
    #View News API
    assert news_View(newsId) == 200, "View News API failed"

    #Update News API
    updateNewsAPI_resp = news_Update(newsId,"Updated Auto News Title")
    assert updateNewsAPI_resp == 200, "Update News API failed"

    #Delete Kiosk API
    assert news_Delete(newsId) == 200, "Delete News API failed"

def testCRUD_Holiday():

    #Holiday List API
    assert holiday_List("2024") == 200,"News List API failed"

    #Create Holiday API
    createHolidayAPI_resp,holidayId = holiday_Create("test Auto holiday","2024-12-16","5608b972-2f93-4330-a2e8-83bad4c9fa84") #date format yyyy-mm-dd , branch ID here is for the default branch in TTISH
    assert createHolidayAPI_resp == 201, "create holiday API failed"
    
    #View Holiday API
    assert holiday_View(holidayId) == 200, "View holiday API failed"

    #Update Holiday API
    updateHolidayAPI_resp = holiday_Update(holidayId,"Updated Auto Holiday Title")
    assert updateHolidayAPI_resp == 200, "Update Holiday API failed"

    #Delete Holiday API
    assert holiday_Delete(holidayId) == 200, "Delete Holiday API failed"