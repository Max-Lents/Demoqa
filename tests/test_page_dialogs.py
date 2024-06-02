import time
from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa


def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()


def test_check_count_el(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    assert modal_dialogs.btns_modal_el.check_count_elements(5)


def test_navigation(browser):
    modal_dialogs = ModalDialogs(browser)
    demo = DemoQa(browser)
    modal_dialogs.visit()
    modal_dialogs.refresh()
    modal_dialogs.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    time.sleep(2)
    browser.forward()
    demo.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
