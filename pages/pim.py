import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from config import variables, XPATHs


class PIMTab:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def click_pim(self):
        self.driver.find_element(By.LINK_TEXT, "PIM").click()
        time.sleep(4)

        assert "PIM" in self.driver.find_element(By.TAG_NAME, "h6").text

    def add_employee(self):
        self.driver.find_element(By.XPATH, XPATHs.add_button_xpath).click()
        time.sleep(5)

        self.driver.find_element(By.NAME, "firstName").send_keys(variables.empFirstName)
        self.driver.find_element(By.NAME, "lastName").send_keys(variables.empLastName)

        # use get_attribute("value") to capture dynamic values from webpage
        emp_id = self.driver.find_element(By.XPATH, XPATHs.employee_id_xpath).get_attribute("value")
        print(emp_id)

        self.driver.find_element(By.XPATH, XPATHs.submit_button_xpath).click()
        time.sleep(10)

        # Validate that employee is added successfully

        assert variables.empFullName in self.driver.find_element(By.XPATH, XPATHs.employee_details_name_xpath).text

    def search_employee(self):
        self.driver.find_element(By.XPATH, XPATHs.emp_name_xpath).send_keys(variables.empFirstName)
        self.driver.find_element(By.XPATH, XPATHs.search_button_xpath).click()
        time.sleep(7)
        # validation
        print(self.driver.find_element(By.XPATH, XPATHs.search_results_xpath).text)
        assert "(1) Record Found" in self.driver.find_element(By.XPATH, XPATHs.search_results_xpath).text

    def edit_employee_info(self):
        self.driver.find_element(By.XPATH, XPATHs.edit_button_xpath).click()
        time.sleep(5)

        # Edit info
        self.driver.find_element(By.NAME, "middleName").send_keys(variables.empMiddleName)
        self.driver.find_element(By.XPATH, XPATHs.emp_edit_info_save_xpath).click()
        time.sleep(7)

        # Validate that edited info is displayed
        assert variables.empMiddleName in self.driver.find_element(By.NAME, "middleName").get_attribute("value")

    def delete_employee(self):
        # click on delete button
        self.driver.find_element(By.XPATH, XPATHs.delete_icon_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, XPATHs.delete_confirm_button_xpath).click()
        time.sleep(5)

        # Validate
        assert "No Records Found" in self.driver.find_element(By.XPATH, XPATHs.search_results_xpath).text
