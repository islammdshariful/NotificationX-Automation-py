import time

from pages.frontend import Notice


def test_notification(browser, config):
    f = Notice(browser)
    f.load()
    f.sale_notice()

