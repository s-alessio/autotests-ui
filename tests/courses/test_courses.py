import allure
import pytest
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
import time

from pages.courses.edit_course_page import EditCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.COURSES) # Добавили feature
@allure.story(AllureStory.COURSES) # Добавили story
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.navbar.check_visible("username")
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page:CoursesListPage, create_course_page:CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)

        create_course_page.image_upload_widget.check_visible('create-course-preview',is_image_uploaded=False)
        create_course_page.create_course_form.check_visible("","","","0","0")

        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image('create-course-preview','./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible('create-course-preview',is_image_uploaded=True)
        create_course_page.create_course_form.fill("Playwright","2 weeks","Playwright","100","10")
        create_course_page.create_course_form.check_visible("Playwright", "2 weeks", "Playwright", "100", "10")

        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=False)
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
        )

    @allure.title("Edit course")
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page:CoursesListPage, create_course_page:CreateCoursePage, edit_course_page:EditCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.image_upload_widget.upload_preview_image('create-course-preview',
                                                                    './testdata/files/image.png')
        create_course_page.create_course_form.fill("Playwright", "2 weeks", "Playwright", "100", "10")
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
        )

        courses_list_page.course_view.menu.click_edit(0)
        edit_course_page.edit_course_toolbar_view.check_visible(is_save_course_disabled=False)
        edit_course_page.edit_course_form.check_visible("Playwright", "2 weeks", "Playwright", "100", "10")
        edit_course_page.edit_course_form.fill("Playwright Advanced", "4 weeks", "Playwright not for dummies", "200", "20")
        edit_course_page.edit_course_form.check_visible("Playwright Advanced", "4 weeks", "Playwright not for dummies", "200", "20")
        edit_course_page.edit_course_toolbar_view.check_visible(is_save_course_disabled=False)
        edit_course_page.edit_course_toolbar_view.click_save_course_button()
        courses_list_page.course_view.check_visible(
            index=0, title="Playwright Advanced", max_score="200", min_score="20", estimated_time="4 weeks"
        )

