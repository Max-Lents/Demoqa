import time

from pages.modal_dialogs import ModalDialogs


def test_check_modal(browser):
    modal = ModalDialogs(browser)
    modal.visit()

    modal.btn_small.click()
    time.sleep(2)
    assert modal.small_modal.exist()
    while modal.btn_close_small.exist():
        modal.btn_close_small.click()

    modal.btn_large.click()
    time.sleep(2)
    assert modal.large_modal.exist()
    while modal.btn_close_large.exist():
        modal.btn_close_large.click()






