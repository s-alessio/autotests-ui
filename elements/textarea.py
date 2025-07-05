from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement
import allure

from tools.logger import get_logger
logger = get_logger("TEXTAREA")

class Textarea(BaseElement):

    @property
    def type_of(self) -> str:  # Переопределяем свойство type_of
        return "textarea"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        # Добавили аргумент nth и передеаем его в get_locator
        return super().get_locator(nth, **kwargs).locator('textarea').first

    def fill(self, value: str, nth: int = 0, **kwargs):
        # Добавили аргумент nth и передеаем его в get_locator
        step = f'Fill {self.type_of} "{self.name}" to value "{value}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.fill(value)

    def check_value(self, value: str, nth: int = 0, **kwargs):
        # Добавили аргумент nth и передеаем его в get_locator
        step = f'Checking that {self.type_of} "{self.name}" has a value "{value}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_value(value)