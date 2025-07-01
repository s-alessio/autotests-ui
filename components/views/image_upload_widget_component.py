from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.button import Button
from elements.file_input import FileInput
from elements.icon import Icon
from elements.image import Image
from elements.text import Text


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page)

        self.preview_image = Image(page, '{identifier}-image-upload-widget-preview-image', 'Preview image')

        self.image_upload_info_icon = Icon(page,'{identifier}-image-upload-widget-info-icon', 'Info icon')
        self.image_upload_info_title = Text(page,'{identifier}-image-upload-widget-info-title-text', 'Info title')
        self.image_upload_info_description = Text(page,
            '{identifier}-image-upload-widget-info-description-text', 'Info description'
        )

        self.upload_button = Button(page, '{identifier}-image-upload-widget-upload-button', 'Upload')
        self.remove_button = Button(page, '{identifier}-image-upload-widget-remove-button', 'Remove')
        self.upload_input = FileInput(page, '{identifier}-image-upload-widget-input', 'Upload')

    # Проверяет отображение виджета в зависимости от наличия загруженного изображения
    def check_visible(self, identifier: str, is_image_uploaded: bool = False):
        self.image_upload_info_icon.check_visible(identifier=identifier)

        self.image_upload_info_title.check_visible(identifier=identifier)
        self.image_upload_info_title.check_have_text('Tap on "Upload image" button to select file',identifier=identifier)

        self.image_upload_info_description.check_visible(identifier=identifier)
        self.image_upload_info_description.check_have_text('Recommended file size 540X300',identifier=identifier)

        self.upload_button.check_visible(identifier=identifier)


        if is_image_uploaded:
            # Если картинка загружена, проверяем состояние специфичное для загруженной картинки
            self.remove_button.check_visible(identifier=identifier)
            self.preview_image.check_visible(identifier=identifier)
        else:
            # Если картинка не загружена, проверяем наличие компонента EmptyViewComponent
            self.preview_empty_view.check_visible(
                identifier=identifier,
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )

    def click_remove_image_button(self, identifier: str):
        self.remove_button.click(identifier=identifier)

    def upload_preview_image(self, identifier: str, file: str):
        self.upload_input.set_input_files(file,identifier=identifier)