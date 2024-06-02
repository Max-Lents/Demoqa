import time

from pages.tables import Tables


def test_add(browser):
    page_tables = Tables(browser)
    page_tables.visit()

    for header in page_tables.headers:
        header.click()


