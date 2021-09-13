from pages.createnotice import AddNew
from pages.wploginpage import WpLoginPage


def test_create(browser, config):

    wp_login = WpLoginPage(browser)
    nx_add = AddNew(browser)

    wp_login.load()
    wp_login.login(config)

    nx_add.nx_load()
    nx_add.create_sale_notice('woo')
    nx_add.nx_load()
    nx_add.create_comment_notice()
    nx_add.nx_load()
    nx_add.create_review_notice('wp')
    nx_add.nx_load()
    nx_add.create_review_notice('woo')
    nx_add.nx_load()
    nx_add.create_download_stat_notice()
    nx_add.nx_load()
    nx_add.create_e_learning_notice()
    nx_add.nx_load()
    nx_add.create_donation_notice()
    nx_add.nx_load()
    nx_add.create_contact_notice('cf7')
    nx_add.nx_load()
    nx_add.create_email_subs_notice()
    nx_add.nx_load()
    nx_add.create_notificationbar('nxbarel')
    nx_add.nx_load()
    nx_add.create_notificationbar('nxbar')
    # nx_add.create_custom_notice()
