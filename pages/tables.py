
from pages.base_page import BasePage

from components.components import WebElement


class Tables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.headers = WebElement(driver, 'div.rt-tr')
        self.header = WebElement(driver, 'div.rt-th')
        # self.row = WebElement(driver, 'div.rt-tbody > div.rt-tr-group > div.rt-td')
        self.row = WebElement(driver, 'div.rt-tbody > div.rt-tr-group:nth-child(4)')
        self.edit = WebElement(driver, 'div.action-buttons > #edit-record-4')
        self.btn_delete = WebElement(driver, 'div.action-buttons > span:nth-child(2) > delete-record-4')

        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, 'div.action-buttons > span:nth-child(2)')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.form_registration = WebElement(driver, 'div.modal-content')

        self.btn_submit = WebElement(driver, 'button#submit')
        self.first_name = WebElement(driver, 'input#firstName')
        self.last_name = WebElement(driver, 'input#lastName')
        self.email = WebElement(driver, 'input#userEmail')
        self.age = WebElement(driver, 'input#age')
        self.salary = WebElement(driver, 'input#salary')
        self.department = WebElement(driver, 'input#department')

