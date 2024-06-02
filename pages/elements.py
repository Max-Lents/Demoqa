from components.components import WebElement
from pages.base_page import BasePage


class Elements(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoga.com/elements'
        super().__init__(driver, self.base_url)

        self.text_middle = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6')
        self.text_elements = WebElement(driver, 'div.playgound-header > div')
        self.icon = WebElement(driver, 'header > a > img')
        self.btn_sidebar_first = WebElement(driver, 'div.left-pannel > div.accordion > div > span > div.header-wrapper')
        self.btn_sidebar_first_textbox = WebElement(driver, '.left-pannel ul.menu-list .btn .text')
        self.btn_sidebar_first_checkbox = WebElement(driver, '.left-pannel ul.menu-list .btn .text')
        self.btns_first_menu = WebElement(driver, 'div:nth-child(1) > div > ul > li')
