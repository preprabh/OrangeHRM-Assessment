from config.variables import username, password, url
from pages.login import LoginPage
from pages.pim import PIMTab

login_page = LoginPage(username, password, url)
driver = login_page.login()

pim_tab = PIMTab(driver)
pim_tab.click_pim()
