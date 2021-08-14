from pages.addnew import AddNew
from pages.wploginpage import WpLoginPage


def test_notification(browser, config):

    wp_login = WpLoginPage(browser)
    nx_add = AddNew(browser)

    wp_login.load()
    wp_login.login(config)

    nx_add.load()
    # nx.add_sale_notification('woo')
    # nx_add.create_comment_notification()
    # nx_add.create_review_notification('wp')
    # nx_add.create_review_notification('woo')
    # nx_add.create_download_stat_notification()
    # nx_add.create_e_learning_notification()
    # nx_add.create_donation_notification()
    nx_add.create_contact_notification('cf7')
