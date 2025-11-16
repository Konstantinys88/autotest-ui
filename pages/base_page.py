import pytest
import allure
from playwright.sync_api import expect, Page

class BasePage():
    def __init__(self, page: Page):
        self.page = page
        
    def visit(self, url: str):
        with allure.step(f"Открываем страницу {url}"):
            self.page.goto(url, wait_until="networkidle")
        
    def reload(self):  # Метод для перезагрузки страницы
        with allure.step(f"Перезагрузка страницы {self.page.url}"):
            self.page.reload(wait_until='domcontentloaded')
            