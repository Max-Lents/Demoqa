from pages.elements import Elements


def test_navigation(browser):
    elements = Elements(browser)
    elements.visit()
    assert elements.btns_first_menu.check_count_elements(9)
