from pages.addnew import AddNew
from pages.wploginpage import WpLoginPage


def test_sale_notification(browser, config):

    wp_login = WpLoginPage(browser)
    nx = AddNew(browser)

    wp_login.load()
    wp_login.login(config)

    nx.load()
    nx.add_sale_notification('woo')
