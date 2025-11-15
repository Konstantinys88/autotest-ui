import pytest
import allure
from playwright.sync_api import expect, Page
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpick
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeature
from allure_commons.types import Severity





@pytest.mark.regression
@allure.title('Создание курса')
@allure.epic(AllureEpick.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStories.STORIES)
@allure.tag(AllureTag.REGRESSION)
@allure.severity(Severity.BLOCKER)
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    with allure.step('Open: https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    with allure.step('проверка заголовка'):
        create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form('','','','0','0')
    create_course_page.check_visible_exercises_title() 
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image('./testdata/files/DataFile.png')
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form('Playwright', "2 weeks", "Playwright",  "100", "10")
    create_course_page.click_create_course_button()
    
    courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    # courses_list_page.check_visible_course_card(0, 'Playwright', "100", "10", "2 weeks")
    courses_list_page.course_view.check_visible(0, 'Playwright', "100", "10", "2 weeks")