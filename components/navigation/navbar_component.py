from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
import allure


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = page.get_by_test_id('navigation-navbar-app-title-text')
        self.welcome_title = page.get_by_test_id('navigation-navbar-welcome-title-text')

    def check_visible(self, username: str):
        with allure.step(f"check_visible UI Course"):
            expect(self.app_title).to_be_visible()
            expect(self.app_title).to_have_text('UI Course')
            
        with allure.step(f"check_visible Welcome, {username}!"):
            expect(self.welcome_title).to_be_visible()
            expect(self.welcome_title).to_have_text(f'Welcome, {username}!')
