from config.variables import url, username, password
from pages.login import LoginPage
from pages.pim import PIMTab

login_page = LoginPage(username, password, url)
driver = login_page.login()

pim_tab = PIMTab(driver)
pim_tab.click_pim()
pim_tab.search_employee()
pim_tab.edit_employee_info()



