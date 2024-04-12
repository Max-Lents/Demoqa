
from pages.base_page import BasePage

from components.components import WebElement
class DemoQa(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.footer = WebElement(driver, 'footer == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."')
        self.middle = WebElement(driver, 'header .row .col-12.mt-4.col-md-6 == "Please select an item from left to start practice."')

    
    # def exist_icon(self):
    #     try:
    #         self.icon.find_element()
    #     except NoSuchElementException:
    #         return False
    #     return True
    # def click_on_the_icon(self):
    #     self.find_element(locator='#app > header > a').click()
    #
    # def click_on_the_btn(self):
    #     self.find_element(locator='#app > div > div > div.home-body > div > div:nth-child(1)').click()

