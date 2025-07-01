from base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.read_config import ConfigReader
from pages.admin_page import AdminPage
import time
class TestAdminUI(BaseTest):
    def test_admin_visible_on_navbar(self):
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        admin_page = AdminPage(self.driver)
        login_page.enter_username(ConfigReader.get_username())
        login_page.enter_password(ConfigReader.get_password())
        login_page.click_login()

        assert dashboard_page.is_admin_tab_visible(), "Admin tab is not visible on left navbar"

        dashboard_page.click_admin_tab()
        time.sleep(4)
        assert admin_page.is_admin_page(), "This is Admin page"
        
        new_user = ConfigReader.get_new_user()
        self.driver.implicitly_wait(15)
        admin_page.add_new_user(
            vacancy_name=new_user["employee-name"],
            username=new_user["new-username"],
            password=new_user["new-password"],
            role=new_user["role"],
            status=new_user["status"]
        )
        self.driver.implicitly_wait(15)
        search_username = ConfigReader.get_search_user()
        assert admin_page.search_user(search_username)
