import time

from pages.demoqa import DemoQa

def test_check_text(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    time.sleep(2)
    demo_qa_page.footer.get_text()
    time.sleep(2)
    demo_qa_page.btn_elements.click()
    time.sleep(2)
    demo_qa_page.middle.get_text()


