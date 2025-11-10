import pytest

from pages.dashboard_page import DashboardPage


def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    dashboard_page_with_state.check_visible_students_char()
    dashboard_page_with_state.sidebar.check_visible()