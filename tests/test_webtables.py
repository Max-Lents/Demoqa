import time

from pages.tables import Tables


def test_tables(browser):
    """Проверка блока No rows found"""
    page_tables = Tables(browser)

    page_tables.visit()
    assert not page_tables.no_data.exist()

    """ Удаляем все записи """
    while page_tables.btn_delete_row.exist():
        page_tables.btn_delete_row.click()

    time.sleep(2)
    assert page_tables.no_data.exist()


def test_add(browser):
    page_tables = Tables(browser)
    page_tables.visit()
    time.sleep(2)
    assert page_tables.btn_add.exist()
    page_tables.btn_add.click()
    time.sleep(2)
    assert page_tables.form_registration.exist()
    page_tables.btn_submit.click_force()
    time.sleep(2)
    assert page_tables.form_registration.exist()
    page_tables.first_name.send_keys('tester')
    page_tables.last_name.send_keys('testerovich')
    page_tables.email.send_keys('name@example.com')
    page_tables.age.send_keys('20')
    page_tables.salary.send_keys('100000')
    page_tables.department.send_keys('text')
    page_tables.btn_submit.click_force()
    time.sleep(5)
    assert not page_tables.form_registration.exist()
    # assert page_tables.row.exist()
    # for element in page_tables.row.find_elements():
    # assert page_tables.row.alert().text == 'tester\ntesterovich\nname@example.com\n20\n100000\ntext'
    page_tables.edit.click_force()
    time.sleep(2)
    assert page_tables.form_registration.exist()
    page_tables.first_name.send_keys('test')
    page_tables.last_name.send_keys('testerov')
    page_tables.btn_submit.click_force()
    time.sleep(5)
    assert not page_tables.form_registration.exist()
    while page_tables.btn_delete.exist():
        page_tables.btn_delete.click()
