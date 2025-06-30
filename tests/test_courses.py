import pytest
from playwright.sync_api import expect
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Verify elements of Courses page (this page can be shown to authorized user only)

    courses_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    courses_list_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(courses_list_icon).to_be_visible()

    courses_empty_list_title_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(courses_empty_list_title_text).to_be_visible()
    expect(courses_empty_list_title_text).to_have_text("There is no results")

    courses_empty_list_desc_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(courses_empty_list_desc_text).to_be_visible()
    expect(courses_empty_list_desc_text).to_have_text("Results from the load test pipeline will be displayed here")

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page:CoursesListPage, create_course_page:CreateCoursePage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form("","","","0","0")
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image("./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)
    create_course_page.fill_create_course_form("Playwright","2 weeks","Playwright","100","10")
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(0,"Playwright","100","10","2 weeks")


