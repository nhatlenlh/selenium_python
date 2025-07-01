from base_test import BaseTest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.read_config import ConfigReader
from pages.admin_page import AdminPage
from pages.recruitment_page import RecruitmentPage
import time

class TestRecruitment(BaseTest):
    def test_is_on_recruitment_page(self):
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        recruitment_page = RecruitmentPage(self.driver)
        login_page.enter_username(ConfigReader.get_username())
        login_page.enter_password(ConfigReader.get_password())
        login_page.click_login()
        self.driver.implicitly_wait(15)
        dashboard_page.click_recruitment_tab()
        time.sleep(3)
        recruitment_page.click_vacancies_tab()
        recruitment_page.click_add_button()
        time.sleep(2)
        new_vacancy_user = ConfigReader.get_new_vacancy()
        recruitment_page.add_new_vacancy(
            vacancy_name=new_vacancy_user["vacancy_name"],
            description=new_vacancy_user["description"],
            hiring_manager=new_vacancy_user["hiring_manager"],
            num_position=new_vacancy_user["num_position"],
        )
        time.sleep(4)