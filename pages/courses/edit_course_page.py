from playwright.sync_api import Page, expect

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.edit_course_toolbar_view_component import EditCourseToolbarViewComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage


class EditCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page)
        self.edit_course_form = CreateCourseFormComponent(page)
        self.edit_course_toolbar_view = EditCourseToolbarViewComponent(page)
        self.create_course_exercises_toolbar_view = CreateCourseExercisesToolbarViewComponent(page)
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)
