import pytest
from assertpy import soft_assertions

from pages.email_subs_notice import EmailSubscription
from pages.manage_notice import Manage


@pytest.mark.order(1)
def test_email_subscription_notice(browser):
    email_subs = EmailSubscription(browser)
    email_subs.load()
    email_subs.create_email_subs_notice('mc', 'n', 'y', 'R')  # Source - Advanced Design - Queue Management - Position


@pytest.mark.order(2)
def test_duplicate_n_update_notice(browser):
    mg = Manage(browser)
    with soft_assertions():
        mg.duplicate_notice()
        mg.update_notice()


@pytest.mark.order(3)
def test_disable_enable_notice(browser):
    mg = Manage(browser)
    with soft_assertions():
        mg.disable_notice('single')
        mg.enable_notice('single')
        mg.disable_notice('bulk')
        mg.enable_notice('bulk')


@pytest.mark.order(4)
def test_shortcode_regenerate_cross_domain_notice(browser):
    mg = Manage(browser)
    with soft_assertions():
        mg.create_shortcode()
        mg.cross_domain_notice('single')
        mg.regenerate_notice('single')
        mg.regenerate_notice('bulk')


@pytest.mark.order(5)
def test_delete_notice(browser):
    mg = Manage(browser)
    with soft_assertions():
        mg.delete_notice_from_edit_page()
        mg.delete_notice('single')
        mg.delete_notice('bulk')
