from pages.addnew import AddNew
from pages.wploginpage import WpLoginPage


def test_login_to_wordpress(browser, config):
    wplog = WpLoginPage(browser)
    nx = AddNew(browser)

    wplog.load()
    wplog.login(config)

    nx.load()
    nx.add_sale_notification('woo')
