from pages.addnew import AddNew
from pages.wploginpage import WpLoginPage


def test_notification(browser, config):

    wp_login = WpLoginPage(browser)
    nx_add = AddNew(browser)

    wp_login.load()
    wp_login.login(config)

    nx_add.load()
    # nx.add_sale_notification('woo')
    nx_add.create_comment_notification()
