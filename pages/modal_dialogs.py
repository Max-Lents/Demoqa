from pages.base_page import BasePage
from components.components import WebElement
from pages.alerts import Alerts


class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_modal_el = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, 'header > a > img')
        self.btn_small = WebElement(driver, '#showSmallModal')
        self.btn_large = WebElement(driver, '#showLargeModal')
        self.small_modal = WebElement(driver, '.modal-content > div > #example-modal-sizes-title-sm')
        self.large_modal = WebElement(driver, '.modal-content > div > #example-modal-sizes-title-lm')
        self.btn_close_small = WebElement(driver, 'button#closeSmallModal')
        self.btn_close_large = WebElement(driver, 'button#closeLargeModal')
