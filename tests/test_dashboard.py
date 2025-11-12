import pytest
from playwright.sync_api import Page, expect
from pages.dashboard_page import DashboardPage
from pages.courses_list_page import CoursesListPage


def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    dashboard_page_with_state.check_visible_students_char()
    dashboard_page_with_state.sidebar.check_visible()
    dashboard_page_with_state.navbar.check_visible("username")
    
    

def test_empty_courses_list(chromium_page_with_state: Page, dashboard_page_with_state: DashboardPage, courses_list_page: CoursesListPage):  
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    dashboard_page_with_state.sidebar.check_visible()
    dashboard_page_with_state.navbar.check_visible("username")
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_empty_view()



    
    
