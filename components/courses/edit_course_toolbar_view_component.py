from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class EditCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page,'create-course-toolbar-title-text', 'Title')
        self.save_course_button = Button(page,'create-course-toolbar-create-course-button', 'Save course')

    def check_visible(self, is_save_course_disabled=True):
        self.title.check_visible()
        self.title.check_have_text('Update course')

        self.save_course_button.check_visible()

        if is_save_course_disabled:
            self.save_course_button.check_disabled()
        else:
            self.save_course_button.check_enabled()

    def click_save_course_button(self):
        self.save_course_button.click()

