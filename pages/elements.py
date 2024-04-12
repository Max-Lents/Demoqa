from pages.base_page import BasePage

class Elements(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoga.com/elements'
        super().__init__(driver, self.base_url)

