from pages.text_box import TextBox
import time


def test_text_box(browser):
    text_box = TextBox(browser)
    text_box.visit()
    text_box.name.send_keys('tester')
    text_box.email.send_keys('tester@exmp.com')
    text_box.btn_submit.click_force()
    time.sleep(2)
    assert text_box.name.get_text() == 'tester'
    assert text_box.email.get_text() == 'tester@exmp.com'

