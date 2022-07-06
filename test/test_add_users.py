from pages.adduser import AddUser
from pages.wploginpage import WpLoginPage


def skip_test_notification(browser, config):

    wp_login = WpLoginPage(browser)
    user_add = AddUser(browser)

    wp_login.load()
    wp_login.login(config)

    for x in range(6):
        user_add.load()
        user_add.add_users(x)
