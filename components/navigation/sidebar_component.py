import re

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar_item = SidebarListItemComponent(page)

    @allure.step("Check visible sidebar")
    def check_visible(self):
        self.sidebar_item.check_visible('logout', 'Logout')
        self.sidebar_item.check_visible('courses', 'Courses')
        self.sidebar_item.check_visible('dashboard', 'Dashboard')

    @allure.step("Click logout on sidebar")
    def click_logout(self):
        self.sidebar_item.navigate('logout',re.compile(r".*/#/auth/login"))

    @allure.step("Click courses on sidebar")
    def click_courses(self):
        self.sidebar_item.navigate('courses', re.compile(r".*/#/courses"))

    @allure.step("Click dashboard on sidebar")
    def click_dashboard(self):
        self.sidebar_item.navigate('dashboard', re.compile(r".*/#/dashboard"))
