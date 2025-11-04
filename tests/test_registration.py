import pytest
from playwright.sync_api import expect, Page
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.mark.authorization
@pytest.mark.parametrize(
    "email, password", [
        # ('123','123'),
        ('sdfsdfsed','sdaasda'),
        ('sdfsdfsed','sdaasda')
        ]
)
def test_wrong_email_or_password_authorization(login_page: LoginPage, email:str, password:str):
    # login_page = LoginPage(page=chromium_page)
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()
    
    
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):  
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form('name123.emai.ru', 'name123', 'name123')
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_title()
    
    
    # chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    # email_input.fill('user.name@gmail.com')

    # username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    # username_input.fill('username')

    # password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    # password_input.fill('password')

    # registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
    # registration_button.click()

    # dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    # expect(dashboard_title).to_be_visible()
    
    # chromium_page.wait_for_timeout(1000)



# def test_empty_courses_list(chromium_page_with_state, chromium_page: Page):
#     chromium_page.wait_for_timeout(1000)