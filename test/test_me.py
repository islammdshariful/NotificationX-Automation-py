from pages.wploginpage import WpLoginPage


def test_case(browser, config):

    wp_login = WpLoginPage(browser)
    # nx = AddNew(browser)

    wp_login.load()
