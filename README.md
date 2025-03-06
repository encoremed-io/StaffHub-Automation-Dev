# StaffHub Automation

This is a project for EM V2 StaffHub Automation. It is a test suite for StaffHub in Dev env

## Pre-requisites
- Chromium Browser
- Python 3.12.xx or above
- any IDE that supports Python (such as VSCode or PyCharm)
-  Git 

## Installation
1. Clone this repository into a directory of your choosing. Run this command in a terminal :
   - `git clone https://github.com/encoremed-io/StaffHub-Automation-Dev path/to/directory/here`
2. Create your virtual environment first by running this command (while in the directory) :
   - `python -m venv venv`
3. Activate your virtual environment :
   - `venv/Scripts/Activate`
4. run this command to install the required libraries :
   - `pip install -r requirements.txt`
  

## Run
- Do check under testdata/LocalVariables.py file if there are credentials available first. if not, need to populate it
- to perform tests, simply run the following command while in the directory:
  - `pytest`
- you can generate reports with pytest allure. run the following command prior to executing the test suite:
  - `pytest alluredir=allure-results`
- to generate the report, run the following command
  - `allure serve allure-results`
