from selenium import webdriver
from testdata.localvariables import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest



@pytest.fixture(scope="function")
def setup(request):
    #define the driver
    driver1 = webdriver.Chrome()
    driver1.maximize_window()
    driver1.implicitly_wait(10)
    driver1.get("https://staffhub-dev.encoremed.io/ttish/auth/login")
    wait = WebDriverWait(driver1,10)


    #make driver instantiated here available in other classes
    request.cls.driver1 = driver1

    #make wait available in other classes
    request.cls.wait = wait

    yield 
    driver1.close()
