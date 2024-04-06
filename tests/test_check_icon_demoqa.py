import time

from pages.demoqa import DemoQa
def test_check_icon(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    time.sleep(2)
    demo_qa_page.click_on_the_icon()
    time.sleep(2)
    assert demo_qa_page.equal_url()
    time.sleep(2)
    assert demo_qa_page.exist_icon()