import time

from pages.accordion import Accordion


def test_visible_accordion(browser):
    acc = Accordion(browser)
    acc.visit()


def test_visible_el(browser):
    acc = Accordion(browser)
    acc.visit()
    assert acc.el.visible()


def test_click_heading(browser):
    acc = Accordion(browser)
    acc.visit()
    acc.heading.click()
    time.sleep(2)


def test_not_visible_el(browser):
    acc = Accordion(browser)
    acc.visit()
    assert acc.el.visible()
    assert not acc.el.visible()


def test_visible_accordion_default(browser):
    acc = Accordion(browser)
    acc.visit()
    assert not acc.section_1.visible()
    assert not acc.section_2.visible()
    assert not acc.section_3.visible()
