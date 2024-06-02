import time

from pages.demoqa import DemoQa
from pages.elements import Elements


def test_check_text_footer(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    time.sleep(2)
    assert demo_qa_page.text_footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    time.sleep(2)


def test_check_text_middle(browser):
    demo_qa_page = DemoQa(browser)
    el_page = Elements(browser)

    demo_qa_page.btn_elements.click()
    time.sleep(2)
    assert el_page.text_middle.get_text() == "Please select an item from left to start practice."


def test_page_elements(browser):
    el_page = Elements(browser)

    el_page.visit()
    assert not el_page.text_elements.get_text() == 'Elements'

    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()